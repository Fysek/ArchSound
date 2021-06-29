import threading
import time
import logging
import samplesConfig
from pygame import mixer

#mixer.pause() when no channel, no move

#pygame.mixer.Channel.play
#pygame.mixer.Channel.get_busy

DEBUG = 1
UNACTIVE_CHANNEL = 0

class SoundPlayer:
    def __init__(self):
        self.__mixer = mixer.init()
        self.__channel0 = mixer.Channel(0) #channel for space
        self.__channel1 = mixer.Channel(1) #channel for steps
        self.__currentSpaceSample = mixer.Sound('samples/01_molenstraat/space.wav')
        self.__currentStepsSample = mixer.Sound('samples/01_molenstraat/steps.wav')
    
    def __debug_message(self, message):
        logging.info(message)
        if DEBUG:
            print(message)
    
    def __setSamplePaths(self, zone):
        for item in samplesConfig.SAMPLES_CONFIG:
            if item['zone'] == str(zone):
                self.__currentSpaceSample = mixer.Sound(item['space'])
                if (item['steps'] != '') :
                    self.__currentStepsSample = mixer.Sound(item['steps'])
                else:
                    self.__currentStepsSample = ''

        self.__debug_message("Current space sample: " + str(self.__currentSpaceSample))
        self.__debug_message("Current steps sample: " + str(self.__currentStepsSample))

    def playSounds(self, zone, move):
        self.__setSamplePaths(zone)
        
        if(zone != UNACTIVE_CHANNEL):
            if self.__channel0.get_busy() == False:
                self.__channel0.play(self.__currentSpaceSample)
                self.__debug_message("Playing space sample")
        else:
            self.__channel0.stop()
            self.__debug_message("Stopping channel 0")
    
        if(move == True):
            if self.__channel1.get_busy() == False:
                if (self.__currentStepsSample != '') :
                    self.__channel1.play(self.__currentStepsSample) 
                    self.__debug_message("Playing steps sample")   
        else:
            self.__channel1.stop()
            self.__debug_message("Stopping channel 1")
        