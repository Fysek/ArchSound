import sys
import logging
from sliderScanner import SliderScanner
from soundPlayer import SoundPlayer
from datetime import datetime

def timeNow():
        now = datetime.now()
        current_time = '[' + now.strftime("%Y:%m:%d.%H:%M:%S") + ']'
        return current_time  


if __name__ == "__main__":
    # Start log file
    logging.basicConfig(filename='/var/log/archsound/' + 'log_' + timeNow() + '.log', level=logging.DEBUG)
    sliderScanner = SliderScanner()
    soundPlayer = SoundPlayer()
    while True:
        try:
            sliderScanner.readValues()
            sliderScanner.evaluateValues()
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
