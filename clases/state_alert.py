

from clases.sound import Sound


class State_Alert:
    
    def __init__(self, sound:Sound):
        self.num_pushButton=0
        self.alarm_activate=False
        self.alarm=sound
        
    #Debounce
        
    def state(self):
        self.num_pushButton+=1
        if self.alarm_activate:
            self.alarm.stop()
            self.num_pushButton=0
            self.alarm_activate=False
        if not self.alarm_activate and self.num_pushButton>=3:
            self.alarm.loop()
            self.alarm_activate=True