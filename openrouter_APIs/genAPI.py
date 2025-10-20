#Imports
import os
import pip
import requests

from google import genai
from google.genai import types

#API Keys
API_KEY = ""

# General API superclass
class GenAPI:
    key = ""
    headers = None
    client = None
    prompt = ""
    history = []
    model = ""

    def __init__(self, API_KEY, model):
        self.key = API_KEY
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        self.model = model
        self.headers = headers

    def respond(self, prompt, model):
        messages = [{"role": "system", "content": prompt["parts"]}]
        while True:
            if prompt["parts"].lower() == "quit":
                break                        
            completion = self.client.chat.completions.create(
                model=model,
                messages=messages
            )
            reply = completion.choices[0].message.content
            print(reply)
            print()
            messages.append({"role": "assistant", "content":reply})
            user_input = input()
            prompt["parts"] = user_input
            messages.append({"role": "user", "content": user_input})
        messages = [{"role": "system", "content": prompt["parts"]}]