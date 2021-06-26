import sys
import logging
from sliderScanner import SliderScanner


if __name__ == "__main__":
    sliderScanner = SliderScanner()
    while True:
        try:
            sliderScanner.readValues()
            sliderScanner.evaluateValues()
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
