import threading, time


    
class Debounce():
    def __init__(self,value:list,delay:int,callback):
        self.value_actually=value
        self.delay=delay
        self.callback=callback
        self.cont=0 #mejor usar time()
        self.thread=threading.Thread(name='Debounce', target=self.__target,daemon=True)
        
    def __target(self):
        while True:
            self.__value_copy=self.value_actually.copy()
            if self.value_actually!=self.__value_copy:
                self.cont=0
                while self.cont<self.delay:
                    time.sleep(0.5)
                    self.cont+=0.5
                    self.__value_copy=self.value_actually.copy()
                    if self.value_actually!=self.__value_copy:
                        self.cont=0
                        pass
                self.callback()
            else:
                time.sleep(0.5)
        
        
    def run(self):
        if not self.thread.is_alive():
            self.thread.start()
        
    def setValue(self,value:list):
        self.value_actually=value
        
    def setDelay(self,delay:int):
        self.delay=delay
        
    def setCallback(self,callback):
        self.callback=callback
            
