#!/usr/bin/python3
import busio
import digitalio
import board
import time
import collections
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
#Only SIX ports are used on each MCP3008
#Read values 
#


DEBUG = 1
LOW_VALUE_BORDER = 64

class SliderScanner():
    def __init__(self, readInterval=1.0):
        self.__spi0 = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        self.__spi1 = busio.SPI(clock=board.SCK_1, MISO=board.MISO_1, MOSI=board.MOSI_1)
        self.__cs0_0 = digitalio.DigitalInOut(board.D8)
        self.__cs0_1 = digitalio.DigitalInOut(board.D18)
        self.__mcp0 = MCP.MCP3008(self.__spi0, self.__cs0_0)
        self.__mcp1 = MCP.MCP3008(self.__spi1, self.__cs0_1)
        self.__timeInterval = readInterval
        self.__timeInterval = 0.2
        self.__channels0 = [0]*6
        self.__channels1 = [0]*5
        self.__values = [0]*11
        self.__move = 0
        self.__activeTable = [False]*11
        self.__currentActiveChannel = 0 #Number from 1-11
        self.__lastReadingsActiveChannel = collections.deque(maxlen=10)
        self.__lastReadingsActiveChannel = [0]*10
        #MCP3008 #1
        self.__channels0[0] = AnalogIn(self.__mcp0, MCP.P0)
        self.__channels0[1] = AnalogIn(self.__mcp0, MCP.P1)
        self.__channels0[2] = AnalogIn(self.__mcp0, MCP.P2)
        self.__channels0[3] = AnalogIn(self.__mcp0, MCP.P3)
        self.__channels0[4] = AnalogIn(self.__mcp0, MCP.P4)
        self.__channels0[5] = AnalogIn(self.__mcp0, MCP.P5)
        #MCP3008 #2
        self.__channels1[0] = AnalogIn(self.__mcp1, MCP.P0)
        self.__channels1[1] = AnalogIn(self.__mcp1, MCP.P1)
        self.__channels1[2] = AnalogIn(self.__mcp1, MCP.P2)
        self.__channels1[3] = AnalogIn(self.__mcp1, MCP.P3)
        self.__channels1[4] = AnalogIn(self.__mcp1, MCP.P4)

    
    def __debug_message(self, message):
        if DEBUG:
            print(message)
               
    def __isMoving(self):
        """
        Deque stores new values at the end
        Comparing last and penultimate reading
        """
        if(self.__lastReadingsActiveChannel[-1] > self.__lastReadingsActiveChannel[-2]):
            return True
        else:
            return False
            
    def __isActiveTenTimes(self):
        """
        Checks if the current channel is active for last ten measurements
        """
        if(sum(self.__lastReadingsActiveChannel) > (LOW_VALUE_BORDER * 10)):
            return True
        else:
            return False            
                           
    def readValues(self):
        self.__debug_message("-----------------")
        
        #Scanning first MCP3008
        for i in range(6): self.__values[i] = self.__channels0[i].value
        time.sleep(self.__timeInterval) 
        #Scanning second MCP3008
        for i in range(5): self.__values[i+6] = self.__channels1[i].value
        time.sleep(self.__timeInterval)
        
        ### DEBUG  
        self.__debug_message(str(self.__values[0:6]) + ' | ' + str(self.__values[6:11]))
        ###
       
    def evaluateValues(self):
        """
        Return active channel; 0 if nothing is acttive
        Return move flag
        """
        # No channel assigned
        if self.__currentActiveChannel == 0:
            for i in range(11):
                if self.__values[i] > LOW_VALUE_BORDER:
                    #self.__activeTable[i] = True # Do we need it?
                    self.__currentActiveChannel = i+1                   
                #else:
                    #self.__activeTable[i] = False     
        else: ## Channel already assigned
        
            currentReading = self.__values[self.__currentActiveChannel-1]
            self.__lastReadingsActiveChannel.append(currentReading)
            
            if (currentReading > LOW_VALUE_BORDER): #active
                self.__move = self.__isMoving()
            else: # not active
                self.__move = 0
                if not self.__isActiveTenTimes():
                    self.__currentActiveChannel = 0
                    self.__lastReadingsActiveChannel = [0]*10
                 
        ### DEBUG   
        self.__debug_message("Active table: " + str(self.__activeTable))
        self.__debug_message("Current active channel: " + str(self.__currentActiveChannel))
        self.__debug_message("Last readings: " + str(self.__lastReadingsActiveChannel))      
        self.__debug_message("Move: " + str(self.__move))
        ###
        
        return self.__currentActiveChannel, self.__move
        