from revChatGPT.V3 import Chatbot
from gtts import gTTS
from playsound import playsound
from os import remove

class Bot:
    _PROMPT: str
    _CHATBOT: Chatbot
    _ANSWER_AUDIO = "./audio/answer.mp3"
    
    def __init__(self):
        self._CHATBOT = Chatbot(api_key="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")
            
    def set_prompt(self, prompt: str):
        self._PROMPT = prompt
        
        if prompt == "":
            print("Prompt no detectado.")
            exit()
    
    def response(self):
        answer = self._CHATBOT.ask(self._PROMPT)
        tts = gTTS(answer, lang='es', tld='es')
        tts.save(self._ANSWER_AUDIO)
        print("Asistente:", answer)
        
        playsound(self._ANSWER_AUDIO)
        remove(self._ANSWER_AUDIO)
