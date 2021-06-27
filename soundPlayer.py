import threading
import time
import logging
import samplesConfig
from pygame import mixer

#mixer.pause() when no channel, no move

#pygame.mixer.Channel.play
#pygame.mixer.Channel.get_busy

DEBUG = 1

class SoundPlayer:
    def __init__(self):
        self.__mixer = mixer.init()
        self.__channel0 = mixer.Channel(0) #channel for space
        self.__channel1 = mixer.Channel(1) #channel for steps
    
    def __debug_message(self, message):
        logging.info(message)
        if DEBUG:
            print(message)
    
    def playSounds(self, zone, move):
        pass  