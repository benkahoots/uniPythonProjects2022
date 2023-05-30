"""
    Author: Ben Tegoni
    ID: 29728452
    Document: animationClass.py
    Description: Object and Static Variables for Animation Frames stored here.
"""
# Packages
from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
from enum import Enum

# Class Imports
from lightClass import Light

# Enumeration for animation frame arrays
class AnimationENUM(Enum):
    # Gif Animation ENUMs
    EGG = ['GIF/egg_gif/egg-frame-1.pbm', 'GIF/egg_gif/egg-frame-2.pbm']
    EGG_HATCH = ['GIF/egg_hatch_gif/egg-hatch-frame-1.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-2.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-3.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-4.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-5.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-6.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-7.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-8.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-9.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-10.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-11.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-12.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-13.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-14.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-15.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-16.pbm', 'GIF/egg_hatch_gif/egg-hatch-frame-17.pbm']
    EVOL_1_IDLE = ['GIF/evol_1_idle_gif/evol_1_stand_frame-1.pbm', 'GIF/evol_1_idle_gif/evol_1_stand_frame-2.pbm', 'GIF/evol_1_idle_gif/evol_1_stand_frame-3.pbm', 'GIF/evol_1_idle_gif/evol_1_stand_frame-4.pbm', 'GIF/evol_1_idle_gif/evol_1_stand_frame-5.pbm', 'GIF/evol_1_idle_gif/evol_1_stand_frame-6.pbm', 'GIF/evol_1_idle_gif/evol_1_stand_frame-7.pbm', 'GIF/evol_1_idle_gif/evol_1_stand_frame-8.pbm', 'GIF/evol_1_idle_gif/evol_1_stand_frame-9.pbm']
    

# Class/Object Imports
class Animation:
    
    # Init Method + Instance Variables for Class
    def __init__(self):
        self.display = create_PiicoDev_SSD1306()

    # Methods
    # Play an Animation Once (Can be edited later to play more than once)
    def startAnimation(self, enum_):
        # Get the ENUM Array
        animationArray = enum_
        # Loop Through Array Once
        for frame in animationArray:
            self.display.load_pbm(frame, 1)
            self.display.show()
            sleep_ms(100)
            self.display.fill(0)
    
    def screenAnimation(self, enumIndex, petObject, petAge, lights):
        # Modify Screen
        if enumIndex == 0:
            # Info Screen
            self.display.text("WEIGHT: " + petObject.getWeight(), 0, 0, 1)
            self.display.text(petAge, 0, 15, 1)
            self.display.text("EVO.LVL: " + str(petObject.getEvolution()), 0, 30, 1)
            self.display.text("ALIVE: " + str(petObject.isAlive), 0, 45, 1)
            self.display.show()
        if enumIndex == 1:
            # do nothing Pet Screen
            exit
        if enumIndex == 2:
            # Hunger Screen
            self.display.text("HUNGER (0-6)", 20, 0, 1)
            self.display.text(str("%.3f" % petObject.getHunger()), 20, 30, 1)
            self.display.show()
            # Lights
            lights.setLightStatus(petObject.getHunger())
        if enumIndex == 3:
            # Happiness Screen
            self.display.text("HAPPINESS (0-6)", 10, 0, 1)
            self.display.text(str("%.3f" % petObject.getHappiness()), 20, 30, 1)
            self.display.show()
        if enumIndex == 4:
            # Energy Stats
            self.display.text("ENERGY (0-6)", 20, 0, 1)
            self.display.text(str("%.3f" % petObject.getEnergy()), 20, 30, 1)
            self.display.show()
        if enumIndex == 5:
            # Sick Status
            self.display.text("SICK (0-6)", 20, 0, 1)
            self.display.text(str("%.3f" % petObject.getSick()), 20, 30, 1)
            self.display.show()
        if enumIndex == 6:
            # Excretion Status
            self.display.text("POO (0-6)", 20, 0, 1)
            self.display.text(str("%.3f" % petObject.getExcretion()), 20, 30, 1)
            self.display.show()
        
    # Get Methods

    
    # Set Methods

# TESTING CODE
#animation = Animation()
#animation.screenAnimation(0)
#animation.startAnimation(AnimationENUM.EGG.value)

