import json
import re
from app.graph.state import AdState
from app.llm import call_llm
from app.services.oauth import validate_oauth
from app.services.music import validate_music_id
from app.services.tiktok_api import submit_ad


def _safe_json(text: str):
    if not text:
        return None

    text = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)
    except:
        pass

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            return None

    return None


# -----------------------------
# 1️⃣ Intent + Ad Generation
# -----------------------------
def intent_extraction_node(state: AdState):
    prompt = f"""
You are a TikTok Ads expert.

User message:
"{state.conversation[-1]}"

Return ONLY valid JSON.
No markdown.
No explanation.

Schema:
{{
  "campaign_name": "string",
  "objective": "Traffic" | "Awareness" | "Conversions",
  "ad_text": "string",
  "cta": "string"
}}
"""

    raw = call_llm(prompt)
    data = _safe_json(raw)

    if not data:
        state.internal_reasoning.append("LLM failed, fallback used.")
        state.campaign_name = "Generic Campaign"
        state.objective = "Traffic"
        state.ad_text = "Discover something amazing today!"
        state.cta = "Learn More"
        return state

    state.campaign_name = data.get("campaign_name")
    state.objective = data.get("objective")
    state.ad_text = data.get("ad_text")
    state.cta = data.get("cta")

    state.internal_reasoning.append(
        f"Inferred objective as {state.objective}"
    )

    return state


# -----------------------------
# 2️⃣ OAuth Validation
# -----------------------------
def oauth_node(state: AdState):
    result = validate_oauth(state.oauth_token)
    if result["error"]:
        state.error = result
    return state


# -----------------------------
# 3️⃣ Business Rules (FIXED)
# -----------------------------
def business_rule_node(state: AdState):
    if state.error:
        return state

    # 🚨 Music REQUIRED for Conversions
    if state.objective == "Conversions":
        if (
            not state.music_id
            or state.music_id.strip() == ""
            or state.music_id == "string"
        ):
            state.error = {
                "message": "Music ID is required for Conversion campaigns."
            }

    return state


# -----------------------------
# 4️⃣ Music Validation
# -----------------------------
def music_validation_node(state: AdState):
    if state.error:
        return state

    if state.music_id:
        result = validate_music_id(state.music_id)
        if not result["valid"]:
            state.error = {
                "message": result["reason"]
            }

    return state


# -----------------------------
# 5️⃣ Submission
# -----------------------------
def submission_node(state: AdState):
    if state.error:
        return state

    payload = {
        "campaign_name": state.campaign_name,
        "objective": state.objective,
        "creative": {
            "text": state.ad_text,
            "cta": state.cta,
            "music_id": state.music_id
        },
        "oauth_token": state.oauth_token
    }

    response = submit_ad(payload)
    if response.get("error"):
        state.error = response
        return state

    state.final_payload = payload
    return state
