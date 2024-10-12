import threading
import time
import logging
import os
import samplesConfig
from pygame import mixer

DEBUG = 1
UNACTIVE_CHANNEL = 0


class SoundPlayer:
    def __init__(self):
        self.__mixer = mixer.init()
        self.__channel0 = mixer.Channel(0)  # channel for space
        self.__channel1 = mixer.Channel(1)  # channel for steps
        self.__currentSpaceSample = None
        self.__currentStepsSample = None

    def __debug_message(self, message):
        if DEBUG:
            logging.info(message)
            print(message)

    def __setSamplePaths(self, zone):
        """
        Sets self.__currentStepsSample based on zone number

        Parameters
        ----------
        zone : str
            Number of the zone
        """
        for item in samplesConfig.SAMPLES_CONFIG:
            if item["zone"] == str(zone):
                self.__currentSpaceSample = mixer.Sound(item["space"])
                if item["steps"] != "":
                    self.__currentStepsSample = mixer.Sound(item["steps"])
                else:
                    self.__currentStepsSample = None

        self.__debug_message("Current space sample: " + str(self.__currentSpaceSample))
        self.__debug_message("Current steps sample: " + str(self.__currentStepsSample))

    def playSounds(self, zone, move):
        """
        Plays the sound based on zone and move

        Parameters
        ----------
        zone : str
            Number of the zone
        move : bool
            If it is moving the move = True

        """
        self.__setSamplePaths(zone)

        if zone != UNACTIVE_CHANNEL:
            if self.__channel0.get_busy() == False:
                if self.__currentSpaceSample:
                    self.__channel0.play(self.__currentSpaceSample)
                    self.__debug_message("Playing space sample")
        else:
            self.__channel0.stop()
            self.__currentSpaceSample = None
            self.__debug_message("Stopping channel 0")

        if move == True:
            if self.__channel1.get_busy() == False:
                if self.__currentStepsSample:
                    self.__channel1.play(self.__currentStepsSample)
                    self.__debug_message("Playing steps sample")
        else:
            self.__channel1.stop()
            self.__currentStepsSample = None
            self.__debug_message("Stopping channel 1")
