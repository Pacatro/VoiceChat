from revChatGPT.V3 import Chatbot

class Bot:
    _API_KEY: str
    _PROMPT: str
    
    def __init__(self, prompt):
        self._API_KEY = "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"
        self._PROMPT = prompt
        
        if prompt == "":
            print("Prompt no detectado.")
            exit()
    
    def response(self):
        chatbot = Chatbot(api_key=self._API_KEY)

        for data in chatbot.ask(self._PROMPT):
            print(data, end="", flush=True)