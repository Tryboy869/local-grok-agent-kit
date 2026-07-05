import requests

class Agent:
    def __init__(self, model='llama3'):
        self.model = model
        print(f'Agent initialized with {model}')

    def run(self, prompt):
        # Basic mock for local Ollama-like
        return f'Response from {self.model}: {prompt[:50]}...'