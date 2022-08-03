from clases.bell import DoorBell
from clases.bot import SmartBellBot
from clases.data_collection import Collect_data
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

voice=Capture_voice()
assistant=Create_voice()

collector=Collect_data(voice,assistant,image,LIST_IDENTIFIER)

state_alert=State_Alert(alarm)

system=DoorBell(bot,collector,state_alert,LIST_IDENTIFIER)

system.activate()



