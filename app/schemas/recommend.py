from pydantic import BaseModel
from typing import Optional

class RecommendRequest(BaseModel):
    personality: Optional[str] = None
    education: Optional[str] = None
    motive: Optional[str] = None
    age: Optional[int] = None
    present_job: Optional[str] = None
    industry: Optional[str] = None
    time_availability_hours: Optional[int] = None
    free_text: Optional[str] = None
