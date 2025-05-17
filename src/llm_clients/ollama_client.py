from langchain_ollama import ChatOllama

class OllamaClient():
    def __init__(self, model: ChatOllama):
        self.model = model
        self.response = ""

    def query(self, prompt:str):
        self.response = self.model.invoke(prompt).content
        return self.response
