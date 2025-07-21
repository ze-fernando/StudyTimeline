from fastapi import APIRouter
from fastapi import status
from src.schemas.study import StudyPlanRequest
from src.service.gemini import GeminiService

route = APIRouter()
service = GeminiService()


@route.post('/', status_code=status.HTTP_201_CREATED)
def make_timeline(plan: StudyPlanRequest):
    text = service.make_content(plan)
    response = service.call(text)

    return {
        'timeline': response
    }
