import whisper
import os

class Listener:
    _WHISPER_MODEL: str
    _AUDIO_DIR: str
    
    def __init__(self, model = "small") -> None:
        self._WHISPER_MODEL = model
        self._AUDIO_DIR = "./audio/audio.mp3"
        
        if self._WHISPER_MODEL == "" or self._AUDIO_DIR == "":
            self._WHISPER_MODEL = "small"
            self._AUDIO_DIR = "./audio/audio.mp3"
            
    def transcribe_audio(self) -> str:
        model = whisper.load_model(self._WHISPER_MODEL)
        result = model.transcribe(self._AUDIO_DIR, fp16=False)
        
        if(result["text"] == ""):
            return "No ha escuchado nada :(\n"
        
        os.remove(self._AUDIO_DIR)   
        return result["text"]