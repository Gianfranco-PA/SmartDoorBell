from pygame import mixer

class Sound:
    
    def __init__(self,sound_dir,volume:float=1):
        mixer.init()
        self.sound=mixer.Sound(sound_dir)
        self.sound.set_volume(volume)
        
    def one(self):
        self.sound.play(loops=0)
        
    def n_repeat(self,n:int=1):
        self.sound.play(loops=n)
    
    def loop(self):
        self.sound.play(loops=-1)
        
    def stop(self):
        self.sound.stop()
    