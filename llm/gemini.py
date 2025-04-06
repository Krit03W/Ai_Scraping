import os
import google.generativeai as genai
from dotenv import load_dotenv
from langchain.llms.base import LLM

load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

class GeminiLLM(LLM):
    def _call(self, prompt: str, stop=None):
        model = genai.GenerativeModel("gemini-1.5-pro")
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt)
        return response.text.strip()

    @property
    def _llm_type(self):
        return "gemini"
