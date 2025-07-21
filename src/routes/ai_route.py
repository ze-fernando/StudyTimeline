from fastapi import APIRouter

route = APIRouter()

@route.get('/')
def main():
    return {'message': 'hello world'}