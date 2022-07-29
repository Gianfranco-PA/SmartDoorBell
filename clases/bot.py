import threading
import telebot
import time
from clases.image import Capture_image
from clases.sound import Sound

import requests
from pydub import AudioSegment
from pydub.playback import play

class SmartBellBot:
    
    def __init__(self, token:str ,image:Capture_image, alarm:Sound):
        self.instance=telebot.TeleBot(token)
        self.image=image
        self.alarm=alarm
        
        @self.instance.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            self.instance.reply_to(message, str(message.chat.id))

        @self.instance.message_handler(commands=['foto'])
        def send_welcome(message):
            self.__response_foto(message)
            
        @self.instance.message_handler(commands=['alarma'])
        def send_welcome(message):
            self.__response_alarma(message)

        @self.instance.message_handler(commands=['para'])
        def send_welcome(message):
            self.__response_para(message)

        @self.instance.message_handler(func=lambda message: True)
        def echo_all(message):
            self.instance.reply_to(message, message.text)
            
        @self.instance.message_handler(content_types=['voice'])
        def handle_audio(message):
            self.__response_para(message,token)

    def start(self):
        threading.Thread(name="SmartBellBot", target=self.instance.polling,).start()
        
    def set_volume(self,value:float):
        self.sound.set_volume(value)
        
    def send_message(self,id:int,message:str):
        self.instance.send_message(id,message)
    
    def send_photo(self,id:int,photo, message:str):
        self.instance.send_photo(id,photo,message)
    
    def __response_foto(self,message):
        fecha=time.strftime("%c")
        nom_img=fecha + " "+ str(message.chat.id)
        self.instance.send_photo(message.chat.id,self.image.capture(),nom_img)
        
    def __response_alarma(self,message):
        self.alarm.loop()
        
    def __response_para(self,message):
        self.alarm.stop()
        
    def __response_para(self,message,token):
        file_info = self.instance.get_file(message.voice.file_id)
        downloaded_file = self.instance.download_file(file_info.file_path)
        with open('Downloaded_voice.oga', 'wb') as new_file:
            new_file.write(downloaded_file)
        sound_oga=AudioSegment.from_ogg('Downloaded_voice.oga')
        sound_oga.export('Voice_to_transmit.wav',format="wav")
        sound=Sound('Voice_to_transmit.wav')
        sound.one()

    
    

