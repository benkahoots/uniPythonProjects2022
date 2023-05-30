"""
    Author: Ben Tegoni
    ID: 29728452
    Document: lightClass.py
    Description: Object to modify LED lights
"""

# Packages
from PiicoDev_RGB import PiicoDev_RGB, wheel
from PiicoDev_Unified import sleep_ms
from enum import Enum

# ENUMs
class COLOUR(Enum):
    red = [255,0,0] 
    green = [0,255,0]
    blue = [0,0,255]
    yellow = [255,255,0]
    magenta = [255,0,255]
    cyan = [0,255,255]
    white = [255,255,255]
    black = [0,0,0]

# LED Class Object
class Light:
    
    # Init Method + Instance Variables for Class
    def __init__(self):
        # First row of LEDs
        self.light1 = PiicoDev_RGB(id=[0,0,0,0])
        self.light1.setBrightness(50)
        # Second row of LEDs
        self.light2 = PiicoDev_RGB(id=[1,0,0,0])
        self.light2.setBrightness(50)
        

    # Methods / Functions
    def setLightStatus(self, status):
        # Status from 0.000 to 6.000
        counter = 0
        # Light Up 0 LED Green
        if status <= 0:
            # LED Strip 1
            self.light1.setPixel(0, COLOUR.red.value)
            self.light1.setPixel(1, COLOUR.red.value)
            self.light1.setPixel(2, COLOUR.red.value)
            # LED Strip 2
            self.light2.setPixel(0, COLOUR.red.value)
            self.light2.setPixel(1, COLOUR.red.value)
            self.light2.setPixel(2, COLOUR.red.value)
        # Light Up 1 LED Green
        if status >= 1 and status < 2:
            # LED Strip 1
            self.light1.setPixel(0, COLOUR.green.value)
            self.light1.setPixel(1, COLOUR.red.value)
            self.light1.setPixel(2, COLOUR.red.value)
            # LED Strip 2
            self.light2.setPixel(0, COLOUR.red.value)
            self.light2.setPixel(1, COLOUR.red.value)
            self.light2.setPixel(2, COLOUR.red.value)
        # Light Up 2 LED Green
        if status >= 2 and status < 3:
            # LED Strip 1
            self.light1.setPixel(0, COLOUR.green.value)
            self.light1.setPixel(1, COLOUR.green.value)
            self.light1.setPixel(2, COLOUR.red.value)
            # LED Strip 2
            self.light2.setPixel(0, COLOUR.red.value)
            self.light2.setPixel(1, COLOUR.red.value)
            self.light2.setPixel(2, COLOUR.red.value)
        # Light Up 3 LED Green
        if status >= 3 and status < 4:
            # LED Strip 1
            self.light1.setPixel(0, COLOUR.green.value)
            self.light1.setPixel(1, COLOUR.green.value)
            self.light1.setPixel(2, COLOUR.green.value)
            # LED Strip 2
            self.light2.setPixel(0, COLOUR.red.value)
            self.light2.setPixel(1, COLOUR.red.value)
            self.light2.setPixel(2, COLOUR.red.value)
        # Light Up 4 LED Green
        if status >= 4 and status < 5:
            # LED Strip 1
            self.light1.setPixel(0, COLOUR.green.value)
            self.light1.setPixel(1, COLOUR.green.value)
            self.light1.setPixel(2, COLOUR.green.value)
            # LED Strip 2
            self.light2.setPixel(2, COLOUR.green.value)
            self.light2.setPixel(1, COLOUR.red.value)
            self.light2.setPixel(0, COLOUR.red.value)
        # Light Up 5 LED Green
        if status >= 5 and status < 6:
            # LED Strip 1
            self.light1.setPixel(0, COLOUR.green.value)
            self.light1.setPixel(1, COLOUR.green.value)
            self.light1.setPixel(2, COLOUR.green.value)
            # LED Strip 2
            self.light2.setPixel(2, COLOUR.green.value)
            self.light2.setPixel(1, COLOUR.green.value)
            self.light2.setPixel(0, COLOUR.red.value)
        # Light Up 5 LED Green
        if status >= 6:
            # LED Strip 1
            self.light1.setPixel(0, COLOUR.green.value)
            self.light1.setPixel(1, COLOUR.green.value)
            self.light1.setPixel(2, COLOUR.green.value)
            # LED Strip 2
            self.light2.setPixel(2, COLOUR.green.value)
            self.light2.setPixel(1, COLOUR.green.value)
            self.light2.setPixel(0, COLOUR.green.value)
            
        # Display Lights
        self.light1.show()
        self.light2.show()
    
    # Get Methods

    
    # Set Methods
