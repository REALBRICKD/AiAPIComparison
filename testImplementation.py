class TestImplementation:
    def __init__(self, APIList, prompts):
        self.ApiList = APIList
        self.prompts = prompts

    def runTests(self):
        """
        Commented out, meant for continuous conversation.
        for api in self.ApiList:
            api.respond(self.prompt, api.model)
        """
        # Iterate through each API, making them respond to a list of prompts without continuous conversation
        for api in self.ApiList:
            for prompt in self.prompts:
                print(f"API: {api.__class__.__name__}, Model: {api.model}")
                api.respond_single(prompt)
                print("-" * 40)  # Separator between responses
