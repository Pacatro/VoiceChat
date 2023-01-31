import whisper

class Listener:
    _WHISPER_MODEL: str
    _AUDIO_DIR: str
    
    def __init__(self, model = "small", audio_dir = "./audio/audio.mp3") -> None:
        self._WHISPER_MODEL = model
        self._AUDIO_DIR = audio_dir
        
        if self._WHISPER_MODEL == "" or self._AUDIO_DIR == "":
            self._WHISPER_MODEL = "small"
            self._AUDIO_DIR = "./audio/audio.mp3"
            
    def listen_audio(self) -> str:
        model = whisper.load_model(self._WHISPER_MODEL)
        result = model.transcribe(self._AUDIO_DIR)
        
        if(result["text"] == ""):
            return "No ha escuchado nada :(\n"
                
        return result["text"]