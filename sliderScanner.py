#!/usr/bin/python3
import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
#Only SIX ports are used on each MCP3008
#Read values 
#


DEBUG = 1
LOW_VALUE_BOARDER = 64

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
        self.__activeTable = [0]*11
        self.__moveTable = [0]*11
        self.__currentActiveChannel = None #Number from 1-11
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
    
    def readValues(self):
        self.__debug_message("-----------------")
        #Scanning first MCP3008
        for i in range(6):
            self.__values[i] = self.__channels0[i].value
   
        self.__debug_message(self.__values[0:6]) 
        time.sleep(self.__timeInterval) 
        #Scanning second MCP3008
        for i in range(5):
            self.__values[i+6] = self.__channels1[i].value
 
        self.__debug_message(self.__values[6:11])
        time.sleep(self.__timeInterval)  

    def evaluateValues(self):
        for i in range(11):
            if self.__values[i] > LOW_VALUE_BOARDER:
                self.__activeTable[i] = True 
            
         
            