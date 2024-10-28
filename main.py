import logging
import sys
from datetime import datetime

from sliderScanner import SliderScanner
from soundPlayer import SoundPlayer


def timeNow():
    now = datetime.now()
    current_time = "[" + now.strftime("%Y:%m:%d.%H:%M:%S") + "]"
    return current_time


if __name__ == "__main__":
    logging.basicConfig(
        filename="/home/fysek/ArchSound/log/" + "log_" + timeNow() + ".log",
        level=logging.DEBUG,
    )
    sliderScanner = SliderScanner()
    soundPlayer = SoundPlayer()
    logging.info("Succesfully initialized the device")
    while True:
        try:
            sliderScanner.readValues()
            zone, move = sliderScanner.evaluateValues()
            soundPlayer.playSounds(zone, move)
        except KeyboardInterrupt:
            logging.info("Interrupted")
            sys.exit(0)
