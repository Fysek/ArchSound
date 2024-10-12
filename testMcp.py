import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

spi0 = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
spi1 = busio.SPI(clock=board.SCK_1, MISO=board.MISO_1, MOSI=board.MOSI_1)
cs0_0 = digitalio.DigitalInOut(board.D8)
cs0_1 = digitalio.DigitalInOut(board.D18)
mcp0 = MCP.MCP3008(spi0, cs0_0)
mcp1 = MCP.MCP3008(spi1, cs0_1)
channels0 = [0] * 6
channels1 = [0] * 5
# MCP3008 #1
channels0[0] = AnalogIn(mcp0, MCP.P0)
channels0[1] = AnalogIn(mcp0, MCP.P1)
channels0[2] = AnalogIn(mcp0, MCP.P2)
channels0[3] = AnalogIn(mcp0, MCP.P3)
channels0[4] = AnalogIn(mcp0, MCP.P4)
channels0[5] = AnalogIn(mcp0, MCP.P5)
# MCP3008 #2
channels1[0] = AnalogIn(mcp1, MCP.P0)
channels1[1] = AnalogIn(mcp1, MCP.P1)
channels1[2] = AnalogIn(mcp1, MCP.P2)
channels1[3] = AnalogIn(mcp1, MCP.P3)
channels1[4] = AnalogIn(mcp1, MCP.P4)

values = [0] * 11


def readValues(timeInterval=0.5):
    """
    Reads from MCP outputs and saves in values list
    """
    print("-----------------")

    # Scanning first MCP3008
    for i in range(6):
        values[i] = channels0[i].value
    time.sleep(timeInterval)
    # Scanning second MCP3008
    for i in range(5):
        values[i + 6] = channels1[i].value
    time.sleep(timeInterval)

    print(f"All channels: {str(values[0:6])} | {str(values[6:11])}")


while 1:
    readValues()
