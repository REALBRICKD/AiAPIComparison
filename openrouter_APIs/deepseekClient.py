from openai import OpenAI
from openrouter_APIs.genAPI import GenAPI
URL = "https://openrouter.ai/api/v1"

# Set up API subclass for Deepseek
class DeepseekClient(GenAPI):
    def __init__(self, apikey, model):
        super().__init__(apikey, model)
        self.client = OpenAI(api_key=apikey, base_url = "https://openrouter.ai/api/v1")
    # override superclass respond method
    def respond(self, prompt, model): 
        super().respond(prompt, model)