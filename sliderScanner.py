#!/usr/bin/python3
import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
#Only SIX ports are used on each MCP3008

DEBUG = 1

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
        self.__channels = [0]*16
        self.__values = [0]*16
        self.__currentActiveChannel = None
        self.__channels[0] = AnalogIn(self.__mcp0, MCP.P0)
        self.__channels[1] = AnalogIn(self.__mcp0, MCP.P1)
        self.__channels[2] = AnalogIn(self.__mcp0, MCP.P2)
        self.__channels[3] = AnalogIn(self.__mcp0, MCP.P3)
        self.__channels[4] = AnalogIn(self.__mcp0, MCP.P4)
        self.__channels[5] = AnalogIn(self.__mcp0, MCP.P5)
        self.__channels[6] = AnalogIn(self.__mcp0, MCP.P6)
        self.__channels[7] = AnalogIn(self.__mcp0, MCP.P7)
        self.__channels[8] = AnalogIn(self.__mcp1, MCP.P0)
        self.__channels[9] = AnalogIn(self.__mcp1, MCP.P1)
        self.__channels[10] = AnalogIn(self.__mcp1, MCP.P2)
        self.__channels[11] = AnalogIn(self.__mcp1, MCP.P3)
        self.__channels[12] = AnalogIn(self.__mcp1, MCP.P4)
        self.__channels[13] = AnalogIn(self.__mcp1, MCP.P5)
        self.__channels[14] = AnalogIn(self.__mcp1, MCP.P6)
        self.__channels[15] = AnalogIn(self.__mcp1, MCP.P7)
    
    def __debug_message(self, message):
        if DEBUG:
            print(message)
    
    def readValues(self):
        self.__debug_message("-----------------")
        for i in range(6):
            self.__values[i] = self.__channels[i].value
   
        self.__debug_message(self.__values[0:6]) 
        time.sleep(self.__timeInterval) 
    
        for i in range(6):
            self.__values[i+8] = self.__channels[i+8].value
 
        self.__debug_message(self.__values[8:14])
        time.sleep(self.__timeInterval)  
  
  
  
  
  