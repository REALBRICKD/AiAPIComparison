import openai
from openai import OpenAI
from genAPI import GenAPI
API_KEY = "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" 
URL = "https://openrouter.ai/api/v1"

# Set up API subclass for Deepseek
class DeepseekClient(GenAPI):
    def __init__(self):
        super().__init__(API_KEY)
        self.client = OpenAI(api_key=API_KEY, base_url = "https://openrouter.ai/api/v1")
    
    def respond(self, prompt):
        # history = []
        while True:
            print(prompt["parts"])
            messages = [{"role": "user", "parts": prompt["parts"]}]
            response = self.client.chat.completions.create(model = "deepseek/deepseek-chat-v3.1:free", messages = messages)
            responseText = response.choices[0].message.content
            print(responseText)
            print()