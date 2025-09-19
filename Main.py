#Imports
import os
import pip
import requests
import openai
from openai import OpenAI
from google import genai
from google.genai import types

#API Keys
DEEPSEEK_API_KEY = "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"
GEMINI_API_KEY = "AIzaSyD5c-r8gC9CSphD601b0llIZ2DX53ArYEw"

# General API superclass
class genAPI:
    key = ""
    url = ""
    headers = None
    client = None

    def __init__(self, API_KEY, url):
        self.key = API_KEY
        self.url = url
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        self.headers = headers

    def respond(self, prompt):
        pass

# Set up API subclass for Deepseek
class deepseekAPI(genAPI):
    def __init__(self, API_KEY, url):
        super().__init__(API_KEY, url)
        self.client = OpenAI(api_key=API_KEY, base_url=url)
    
    def respond(self, prompt):
        response = self.client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False)
        print(response.choices[0].message.content)

#Set up API subclass for Google Gemini
class googleGeminiAPI(genAPI):
    def __init__(self, API_KEY, url):
        super().__init__(API_KEY, url)
        self.client = genai.Client(api_key=API_KEY)
    
    def respond(self, prompt):
        response = self.client.models.generate_content(
            model="gemini-2.5-pro",
            contents = prompt,
            config = types.GenerateContentConfig(
                thinking_config = types.ThinkingConfig(thinking_budget = 128)
            ),
        )
        print(response.text)

# Executes requests to APIs
class Main:
    APIList = []
    prompt = ""
    def __init__(self, prompt) -> None:
        deepseek = deepseekAPI(DEEPSEEK_API_KEY, "https://openrouter.ai/api/v1")
        gemini = googleGeminiAPI(GEMINI_API_KEY, "")
        self.APIList.append(deepseek)
        self.APIList.append(gemini)

        self.prompt = prompt

    def runTests(self):
        for i in self.APIList:
            i.respond(self.prompt)

main = Main("Hello, how are you?")
main.runTests()