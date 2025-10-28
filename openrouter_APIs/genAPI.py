#API Keys
API_KEY = ""
import logging 

# General API superclass meant for all openrouter APIs.
class GenAPI:
    key = ""
    headers = None
    client = None
    prompt = ""
    history = []
    model = ""
    # Authenticate key
    def __init__(self, API_KEY, model):
        self.key = API_KEY
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        self.model = model
        self.headers = headers
    # Hold continuous conversation with user
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
    # Single response without continuous conversation
    def respond_single(self, prompt):
        message = [{"role": "system", "content": prompt["parts"]}]
        response = self.client.chat.completions.create(model=self.model, messages = message)
        print(prompt["parts"])
        print(response.choices[0].message.content)