from clases.bot import SmartBellBot
from clases.image import Capture_image
from gpiozero import Button
from signal import pause
from clases.sound import Sound
from clases.state_alert import State_Alert
from clases.voice import Capture_voice,Create_voice

from variables import ADMIN,LIST_IDENTIFIER,ALARM_DIR, TOKEN

alarm=Sound(ALARM_DIR)
image=Capture_image(1280,720)
bot=SmartBellBot(TOKEN,image,alarm)
bot.start()

voice=Capture_voice()
assistant=Create_voice()

state_alert=State_Alert(alarm)

def find_floor(word:str):
    word=word.lower()
    for item in LIST_IDENTIFIER:
        values=list(item.values())
        for value in values[0]:
            if value.lower() in word:
                return values[1]
    return False


def process_collection():
    swt=True
    assistant.create("Bienvenido, ¿A quien busca?")
    assistant.run()
    while True:
        input_home=voice.capture(10)
        if not input_home:
            assistant.create("No se escucha ninguna voz. Terminando proceso")
            assistant.run()
            swt=False
            break
        id=find_floor(input_home)
        if id:
            break
        assistant.create("No encuentro coincidencias. ¿Podria decirlo denuevo?")
        assistant.run()
    if swt:
        photo=image.capture()
        bot.send_photo(ADMIN,photo,"Tienes una visita.\nDijo:{}\nIdentificado:{}".format(input_home,id))
        bot.send_photo(id,photo,"Alguien esta buscando a {} en la puerta".format(input_home))
        

button_visitor = Button(17)
button_alarm = Button(23)

button_visitor.when_pressed = process_collection
button_alarm.when_pressed = state_alert.state

pause()
