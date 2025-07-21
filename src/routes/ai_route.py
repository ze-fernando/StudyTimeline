from fastapi import APIRouter

route = APIRouter()

@route.get('/')
def main():
    return {'message': 'hello world'}


@route.post('/')
def make_timeline(plan: StudyPlanRequest):
    return {
        'subjects': plan.subjects,
        'days': plan.availability
    }
