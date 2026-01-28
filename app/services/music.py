import uuid

def upload_custom_music():
    return f"music_{uuid.uuid4().hex[:8]}"

def validate_music_id(music_id: str):
    if music_id == "invalid":
        return {
            "valid": False,
            "reason": "Music ID rejected by API."
        }
    return {"valid": True}
