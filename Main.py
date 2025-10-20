#Imports
from google_APIs.googleGeminiClient import GoogleGeminiClient
from openrouter_APIs.deepseekClient import DeepseekClient
from openrouter_APIs.grokClient import GrokClient
from testImplementation import TestImplementation
from dotenv import load_dotenv
import os

load_dotenv() # Load variables from .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Executes requests to APIs
class Main:
    APIList = []
    prompt = {}
    def __init__(self, prompt) -> None:
        gemini = GoogleGeminiClient(GEMINI_API_KEY, "gemini-2.5-pro") 
        self.APIList.append(gemini)
        deepseek = DeepseekClient(OPENROUTER_API_KEY, "deepseek/deepseek-chat-v3.1:free")
        self.APIList.append(deepseek)
        grok = GrokClient(OPENROUTER_API_KEY, "x-ai/grok-4-fast")
        self.APIList.append(grok)
        self.prompt = prompt

    def run(self):
        testImplementation = TestImplementation(self.APIList, self.prompt)
        testImplementation.runTests()

if __name__ == "__main__":
    main = Main({"role": "user", "parts": "Can you briefly introduce yourself?"})
    main.run()