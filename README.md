<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#idea">Idea</a></li>
        <li><a href="#schematic">Schematic</a></li>
        <li><a href="#software">Software</a></li>
        <li><a href="#result">Result</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- IDEA -->
### Idea

This is a sound player for architectural model and can be used in any other applciation as well. At the end it became a paort of the model for master thesis: _Sonic relation as a design tool_.

The idea of a sound player is to imitate acoustics in the designed spaces. User can touch a membrane which is a potentiometer. This analog value is then converted by MCP3008 to digital and used in the application. Based on reading's location, a particular, characteristic to the area sound is played. Additionally, there is algorithm implemented which plays and stops a sound of footsteps if the user is moving on the membrane. Mind that only one direction of movement (forward) is supported.   

<!-- SCHEMATIC -->
### Schematic

This section 

<!-- SOFTWARE -->
### Software

This section 

<!-- RESULT -->
### Result

This section 

<!-- GETTING STARTED -->
## Getting Started

This chapter contains all information to easily and fast start the application. 

### Prerequisites

For the software point of view, only python packages are needed to run the application.
* execute this command to install all required python packages
  ```sh
  python -m pip install -r requirements
  ```

## Usage
To run the application, simply execute the command below:
```cmd
python ./main.py 
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Mateusz Dyrdol - [@Mateusz Dyrdol](https://www.linkedin.com/in/mateusz-dyrdol/) - mateusz.dyrdol@gmail.com

Project Link: [https://github.com/Fysek/ArchSound/](https://github.com/Fysek/ArchSound/)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Adafruit MCP3008 github](https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx)
* [Analog Inputs using MCP3008](https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi)
* [Multiple MCP3008](https://www.raspberrypi.org/forums/viewtopic.php?t=210330)
* [Pymixer - playing multiple sounds at once](https://classes.engineering.wustl.edu/ese205/core/index.php?title=Playing_multiple_sounds_at_once)
* [Raspberry Pi Multiple SPIs](https://blog.stabel.family/raspberry-pi-4-multiple-spis-and-the-device-tree/)
* [Raspberry Pi Pinout](https://pinout.xyz/pinout/spi)
* [Ultraflat Potentiometer Membrane](https://www.vishay.com/sensors/list/product-32537/)
