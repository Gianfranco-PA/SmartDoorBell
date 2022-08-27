import time
from clases.sound import Sound


class State_Alert:
    
    def __init__(self, sound:Sound):
        self.num_pushButton=0
        self.alarm_activate=False
        self.alarm=sound
        self.__time=0
        
        
    def to_update(self):
        if self.__time>time.time():
            self.__time=time.time()+8
            if self.alarm_activate:
                self.alarm.stop()
                self.num_pushButton=0
                self.alarm_activate=False
            elif not self.alarm_activate and self.num_pushButton>2:
                self.alarm.loop()
                self.alarm_activate=True
            else:
                self.num_pushButton+=1
        else:
            self.__time=time.time()+8
            self.alarm.stop()
            self.alarm_activate=False
            self.num_pushButton=1
            
    def getIsState(self):
        return self.alarm_activate
    