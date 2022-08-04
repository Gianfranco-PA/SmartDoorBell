import threading, time


    
class Debounce():
    def __init__(self,value:list,delay:int,callback):
        self.value_actually=value
        self.delay=delay
        self.callback=callback
        self.cont=0
        self.thread=threading.Thread(name='Debounce', target=self.__target)
        
    def __target(self):
        self.__value_copy=self.value_actually.copy()
        while self.cont<self.delay:
            if self.value_actually!=self.__value_copy:
                self.cont=0
                self.__value_copy=self.value_actually.copy()
                pass
            self.cont+=0.5
            time.sleep(0.5)
            
        self.callback()
        
    def run(self):
        if not self.thread.is_alive():
            self.thread=threading.Thread(name='Debounce', target=self.__target)
            self.thread.start()
        
    def setValue(self,value:list):
        self.value_actually=value
        
    def setDelay(self,delay:int):
        self.delay=delay
        
    def setCallback(self,callback):
        self.callback=callback
            
