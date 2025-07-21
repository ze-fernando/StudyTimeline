from pydantic import BaseModel
from typing import List


class AvailableDay(BaseModel):
    day: str
    hours: float


class StudyPlanRequest(BaseModel):
    subjects: List[str]
    availability: List[AvailableDay]
