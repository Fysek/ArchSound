import sys
import logging
import helper
from SliderScanner import SliderScanner


if __name__ == "__main__":
    sliderScanner = SliderScanner()
    while True:
      sliderScanner.readValues()
