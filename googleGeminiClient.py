from genAPI import GenAPI
from google import genai
from google.genai import types
API_KEY = "AIzaSyD5c-r8gC9CSphD601b0llIZ2DX53ArYEw"

#Set up API subclass for Google Gemini
class GoogleGeminiClient(GenAPI):
    chat = None

    def __init__(self):
        super().__init__(API_KEY)
        self.client = genai.Client(api_key=API_KEY)
        self.chat = self.client.chats.create(model = "gemini-2.5-pro")
    
    def respond(self, prompt):
        history = {} # reset history 
        while True:
            response = self.chat.send_message(prompt["parts"])
            if prompt["parts"].lower() == "quit":
                break
            print(response.text)
            print()
            user_input = input()
            prompt = {"role": "user", "parts": user_input} # get new prompt
            