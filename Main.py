import site

from pydantic.type_adapter import P
site.addsitedir(site.getusersitepackages())

#Imports
from google_APIs.googleGeminiClient import GoogleGeminiClient
from openrouter_APIs.deepseekClient import DeepseekClient
from openrouter_APIs.grokClient import GrokClient
from testImplementation import TestImplementation
import dotenv
from dotenv import load_dotenv
import os

load_dotenv() # Load variables from .env file
GEMINI_API_KEY =  os.getenv("GEMINI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initializes API and prompt list, runs tests
class Main:
    prompts = []
    APIList = []
    def __init__(self, prompts) -> None:
        self.prompts = prompts
        gemini = GoogleGeminiClient(GEMINI_API_KEY, "gemini-2.5-pro") 
        self.APIList.append(gemini)
        deepseek = DeepseekClient(OPENROUTER_API_KEY, "deepseek/deepseek-chat-v3.1")
        self.APIList.append(deepseek)
        grok = GrokClient(OPENROUTER_API_KEY, "x-ai/grok-4-fast")
        self.APIList.append(grok)

    def run(self):
        testImplementation = TestImplementation(self.APIList, self.prompts)
        testImplementation.runTests()

# Read prompts from file, separated by blank lines. Saves them as a list of dictionaries.
def initPrompts(path="prompts.txt"):
    prompts = []
    buf_lines = []
    f = open("prompts.txt")
    # with open(path, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
                buf_lines.append(line)
        else:
            if buf_lines:
                content = "".join(buf_lines).replace("\n", "")
                prompts.append({"role": "user", "parts": content})
                buf_lines = []
    if buf_lines:
        content = "".join(buf_lines).replace("\n", "")
        prompts.append({"role": "user", "parts": content})
    return prompts

if __name__ == "__main__":
    main = Main(initPrompts())
    main.run()