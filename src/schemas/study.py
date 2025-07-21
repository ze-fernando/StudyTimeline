from pydantic import BaseModel

class AvailableDay(BaseModel):
    day: str
    hours: float


class StudyPlanRequest(BaseModel):
    subjects: List[str]
    availability: List[AvailableDay]
