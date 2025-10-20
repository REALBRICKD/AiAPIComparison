class TestImplementation:
    def __init__(self, APIList, prompt):
        self.ApiList = APIList
        self.prompt = prompt

    def runTests(self):
        # Call each API with its own configured model
        for api in self.ApiList:
            api.respond(self.prompt, api.model)