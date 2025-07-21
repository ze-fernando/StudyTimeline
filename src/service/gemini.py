from src.config.settings import settings
from src.schemas.study import StudyPlanRequest
from google import genai


class GeminiService:
    def __init__(self):
        self.client = genai.Client(api_key=settings.API_KEY)

    def call(self, content):
        response = self.client.models.generate_content(
            model='gemini-2.5-flash',
            contents=content
            )

        return response.text

    def make_content(self, payload: StudyPlanRequest):
        text = 'Monte para mim um cronograma de estudo baseado na minha rotina atual.'

        for i, sub in enumerate(payload.subjects):
            text += f'Matéria {i+1} {sub} \n'

        text += 'Tenho disponivel: \n'
        for i, day in enumerate(payload.availability):
            text += f'Na {day.day} {day.hours} horas'

        text += '\n\n OBS: É DE EXTREMA IMPORTANCIA QUE VOCE NAO USE MARKDOWN'
        text += '\n\n OBS: É DE EXTREMA IMPORTANCIA QUE VOCE NAO DIGA NADA ENVIE SO O CRONOGRAMA'

        print(text)

        return text
