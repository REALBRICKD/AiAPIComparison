class TestImplementation:
    ApiList = []
    prompt = {}
    def __init__(self, APIList, prompt):
        self.ApiList = APIList
        self.prompt = prompt

    def runTests(self, prompt):
        for i in self.ApiList:
            self.chat(prompt)

    def chat(self, prompt):
        for api in self.ApiList:
            api.respond(prompt)