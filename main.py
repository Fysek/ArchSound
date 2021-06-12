import sys
import logging
from sliderScanner import SliderScanner


if __name__ == "__main__":
    sliderScanner = SliderScanner()
    while True:
      sliderScanner.readValues()
