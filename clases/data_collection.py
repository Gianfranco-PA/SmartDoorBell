

from clases.image import Capture_image
from clases.voice import Capture_voice, Create_voice



class Collect_data:
    
    def __init__(self,capVoice:Capture_voice, creVoice:Create_voice,capImage:Capture_image,name_list:list):
        self.capVoice=capVoice
        self.creVoice=creVoice
        
        self.capImage=capImage
        
        self.name_list=name_list
        
        
    def __find_floor(self,word:str):
        word=word.lower()
        for item in self.name_list:
            for value in item["Names"]:
                if value.lower() in word:
                    return item["ID_Telegram"]
        return False
    
    def __to_ask(self, question:str, wait_time:int):
        cont=0
        self.creVoice.create(question)
        self.creVoice.run()
        while True:
            input_voice=self.capVoice.capture(wait_time)
            if not input_voice:
                if cont>2:
                    self.creVoice.create("No se detecto ninguna voz. Terminando proceso")
                    self.creVoice.run()
                    return False
                self.creVoice.create("No se detecto ninguna voz. ¿Podria decirlo denuevo?")
                self.creVoice.run()
                cont+=1
            return input_voice
            
    def run(self):
        data={}
        data["Visitor_name"]=self.__to_ask("Bienvenido. ¿Cual es su nombre?",10)
        data["Looks_for"]=self.__to_ask("¿A quien busca?",5)
        data["ID_habitant"]=self.__find_floor(data["Looks_for"])
        while not data["ID_habitant"]:
            qstn="No se encuentran coincidencias para {0}. Por favor podria repetirlo".format(data["Looks_for"])
            data["Looks_for"]=self.__to_ask(qstn,5)
            data["ID_habitant"]=self.__find_floor(data["Looks_for"])
        data["Photo"]=self.capImage.capture()
        return data
            