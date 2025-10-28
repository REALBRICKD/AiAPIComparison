from openrouter_APIs.genAPI import GenAPI
from dotenv import load_dotenv
from openai import OpenAI

# Set up API subclass for Deepseek
class GrokClient(GenAPI):
    def __init__(self, apikey, model):
        super().__init__(apikey, model)
        self.client = OpenAI(api_key=apikey, base_url="https://openrouter.ai/api/v1")
    # override superclass respond method
    def respond(self, prompt, model):
        super().respond(prompt, model)