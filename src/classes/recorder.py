import pyaudio
import wave

class Recorder:
    _FORMAT = pyaudio.paInt16
    _CHANNELS: int
    _RATE: int
    _CHUNK: int
    _FILE: str
    _FRAMES: list
    _AUDIO = pyaudio.PyAudio()
    _STREAM: pyaudio.Stream
    
    def __init__(self, channels = 2, rate = 44100, chunk = 1024) -> None:
        self._CHANNELS = channels
        self._RATE = rate
        self._CHUNK = chunk
        self._FILE = "./audio/question.mp3"
        self._INPUT = True
        self._FRAMES = []
        
        if self._CHANNELS < 0 or self._RATE < 0 or self._CHUNK < 0 or self._FILE == "" or self._FRAMES != []: 
            self._CHANNELS = 2
            self._RATE = 44100
            self._CHUNK = 1024
            self._FILE = "./audio/question.mp3"
            self._FRAMES = []
            
        self._STREAM = self._AUDIO.open(format = self._FORMAT, channels = self._CHANNELS, rate = self._RATE, 
                                        input = self._INPUT, frames_per_buffer = self._CHUNK)

    def rec(self):                
        while True:
            try:
                data = self._STREAM.read(self._CHUNK)
                self._FRAMES.append(data)
            except KeyboardInterrupt:
                break
            
        print("\nFinished recording\n")
        
        self._STREAM.close()
        
        waveFile = wave.open(self._FILE, 'wb')
        waveFile.setnchannels(self._CHANNELS)
        waveFile.setsampwidth(self._AUDIO.get_sample_size(self._FORMAT))
        waveFile.setframerate(self._RATE)
        waveFile.writeframes(b''.join(self._FRAMES))
        waveFile.close()

    