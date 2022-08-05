import speech_recognition as sr

class Capture_voice:
    
    def __init__(self):
        self.recognizer=sr.Recognizer()
        self.microphone=sr.Microphone(device_index=0)
        
    
    def capture(self,time_wait:int):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
        try:
            audio=self.recognizer.listen(source,time_wait)
        except sr.WaitTimeoutError as e:
            print(e)
            return False
        text=self.recognizer.recognize_google(audio,language="es-PE")
        return text
            
            
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

class Create_voice:
    
    def __init__(self):
        self.song=None
    
    def create(self,textForVoice:str):
        tts = gTTS(text=textForVoice, lang='es')
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        #---
        self.song = AudioSegment.from_file(fp, format="mp3")
    def run(self):
        play(self.song)
        
        