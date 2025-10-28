from google import genai
from google.genai import types

#Set up API subclass for Google Gemini
class GoogleGeminiClient():
    chat = None
    model = ""

    def __init__(self, apikey, model):
        self.model = model
        self.client = genai.Client(api_key=apikey)
        self.chat = self.client.chats.create(model = self.model)
    
    # Hold continuous conversation with user
    def respond(self, prompt, model=None):
        while True:
            response = self.chat.send_message(prompt["parts"])
            if prompt["parts"].lower() == "quit":
                break
            print(response.text)
            print()
            user_input = input()
            prompt = {"role": "user", "parts": user_input} # get new prompt

    # Single response without continuous conversation
    def respond_single(self, prompt):
        response = self.chat.send_message(prompt["parts"])
        print(prompt["parts"])
        print(response.text)