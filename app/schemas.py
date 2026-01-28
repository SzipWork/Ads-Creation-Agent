from pydantic import BaseModel
from typing import Optional, Dict, List

class AdRequest(BaseModel):
    user_message: str
    music_id: Optional[str] = None
    oauth_token: Optional[str] = "valid"

class AdResponse(BaseModel):
    conversation: List[str]
    internal_reasoning: List[str]
    final_ad_payload: Optional[Dict]
    error: Optional[Dict]
