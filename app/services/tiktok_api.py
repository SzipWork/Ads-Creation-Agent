def submit_ad(payload: dict):
    if payload.get("oauth_token") == "expired":
        return {
            "error": True,
            "explanation": "OAuth token expired.",
            "action": "Re-authenticate.",
            "retry": True
        }

    if payload["creative"].get("music_id") == "invalid":
        return {
            "error": True,
            "explanation": "Invalid music ID.",
            "action": "Provide a valid music ID.",
            "retry": True
        }

    return {"success": True}
