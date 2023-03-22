from revChatGPT.V3 import Chatbot

class Bot:
    _PROMPT: str
    _CHATBOT: Chatbot
    
    def __init__(self):
        self._CHATBOT = Chatbot(api_key="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")
            
    def set_prompt(self, prompt: str):
        self._PROMPT = prompt
        
        if prompt == "":
            print("Prompt no detectado.")
            exit()
    
    def response(self):
        print("Asistente:", self._CHATBOT.ask(self._PROMPT))
