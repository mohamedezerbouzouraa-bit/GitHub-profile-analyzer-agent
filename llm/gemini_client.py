from google import genai
from config.settings import GEMINI_API_KEY, MODEL

client = genai.Client(api_key=GEMINI_API_KEY)


def generate(prompt: str):
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    return response.text
