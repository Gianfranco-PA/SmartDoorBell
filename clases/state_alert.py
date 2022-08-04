

from clases.sound import Sound
from clases.debounce import Debounce


class State_Alert:
    
    def __init__(self, sound:Sound):
        self.num_pushButton=[0]
        self.alarm_activate=False
        self.alarm=sound
        self.debounce=Debounce(self.num_pushButton,3,self.restart)
        self.debounce.run()
        
        
    def to_update(self):
        self.num_pushButton[0]+=1
        if self.alarm_activate:
            self.alarm.stop()
            self.restart()
            self.alarm_activate=False
        if not self.alarm_activate and self.num_pushButton[0]>=3:
            self.alarm.loop()
            self.alarm_activate=True
            
    def getIsState(self):
        return self.alarm_activate
    
    def restart(self):
        self.num_pushButton=[0]