from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from app.graph.graph import build_graph

app = FastAPI()
graph = build_graph()


class CreateAdRequest(BaseModel):
    user_message: str
    oauth_token: str
    music_id: Optional[str] = None


@app.post("/create-ad")
def create_ad(req: CreateAdRequest):
    state = {
        "conversation": [req.user_message],
        "internal_reasoning": ["User initiated ad creation"],
        "oauth_token": req.oauth_token,
        "music_id": req.music_id,
        "campaign_name": None,
        "objective": None,
        "ad_text": None,
        "cta": None,
        "final_payload": None,
        "error": None
    }

    final_state = graph.invoke(state)

    return {
        "conversation": final_state.get("conversation"),
        "internal_reasoning": final_state.get("internal_reasoning"),
        "final_ad_payload": final_state.get("final_payload"),
        "error": final_state.get("error")
    }
