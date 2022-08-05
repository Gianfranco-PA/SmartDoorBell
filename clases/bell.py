

from gpiozero import Button
from signal import pause
from clases.bot import SmartBellBot
from clases.data_collection import Collect_data
from clases.state_alert import State_Alert


class DoorBell:
    
    def __init__(self, bot:SmartBellBot, collect:Collect_data,alarm:State_Alert, chats_list:list):
        self.bot=bot
        self.collect=collect
        self.alarm=alarm
        self.chats_list=chats_list
        
        self.button_init=Button(17)
        self.button_alarm=Button(23)
        
        self.button_init.when_pressed=self.process_notification
        self.button_alarm.when_pressed=self.emergency_notification
        
    def process_notification(self):
        data=self.collect.run()
        
        msg="""
            Tienes una visita en la puerta.\n
            Nombre:{0}\n
            Busca a: {1}
        """.format(data["Visitor_name"],data["Looks_for"])
        self.bot.send_photo(data["ID_habitant"],data["Photo"],msg)
        self.bot.set_time_respond()
        
    def emergency_notification(self):
        self.alarm.to_update()
        if self.alarm.getIsState():
            for item in self.chats_list:
                self.bot.send_message(item["ID_Telegram"],"SE HA ACTIVADO LA ALARMA. POR FAVOR TENGA CUIDADO")
            
        
    def activate(self):
        self.bot.start()
        pause()