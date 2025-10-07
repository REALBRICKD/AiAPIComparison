#Imports
import os
import pip
import requests
from googleGeminiClient import GoogleGeminiClient
from deepseekClient import DeepseekClient
from grokClient import GrokClient
from testImplementation import TestImplementation

# Executes requests to APIs
class Main:
    APIList = []
    prompt = {}
    def __init__(self, prompt) -> None:
        gemini = GoogleGeminiClient() 
        self.APIList.append(gemini)
        # deepseek = DeepseekClient()
        # self.APIList.append(deepseek)
        # grok = GrokClient()
        # self.APIList.append(grok)
        self.prompt = prompt

    def run(self):
        testImplementation = TestImplementation(self.APIList, self.prompt)
        testImplementation.runTests(self.prompt)

main = Main({"role": "user", "parts": "Can you briefly introduce yourself?"})
main.run()