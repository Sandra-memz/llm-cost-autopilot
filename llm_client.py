import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def call_model(model_id: str, prompt: str) -> str:
    """Send a prompt to a Gemini/Gemma model and return its text answer."""
    response = client.models.generate_content(model=model_id, contents=prompt)
    usage = response.usage_metadata
    return response.text, usage.prompt_token_count or 0, usage.candidates_token_count or 0