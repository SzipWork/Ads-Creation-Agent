from pydantic import BaseModel
from typing import Optional, List, Dict

class AdState(BaseModel):
    conversation: List[str] = []
    internal_reasoning: List[str] = []

    campaign_name: Optional[str] = None
    objective: Optional[str] = None
    ad_text: Optional[str] = None
    cta: Optional[str] = None
    music_id: Optional[str] = None

    oauth_token: Optional[str] = None
    final_payload: Optional[Dict] = None
    error: Optional[Dict] = None
