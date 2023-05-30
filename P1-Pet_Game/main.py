"""
    Author: Ben Tegoni
    ID: 29728452
    Document: main.py
    Description: Main Application proccess running through here.
"""

# Packages
from PiicoDev_Unified import sleep_ms
from PiicoDev_CAP1203 import PiicoDev_CAP1203
import threading

# Class/Object Imports
from timeClass import Time
from petClass import Pet
from animationClass import *
from screenClass import Screen


# Creation of Objects for start of game 
# Creation of time Object
time_object = Time() 
# Creation of Pet Object
pet_object = Pet(time_object.getTimePassed())
# Creation of Animation Object
animation_object = Animation()
# Creation of Screen Object
screen_object = Screen()
# Creation of Light Object
light_object = Light()


# Sensor and PiicoDev Components
touchSensor = PiicoDev_CAP1203(touchmode="single", sensitivity=6) # Touch Capacative Sensor Code

# Condition for game starting
while pet_object.evolutionLvl == 0 and pet_object.isAlive == True:
    # Set First Animation to be the Egg
    animation_object.startAnimation(AnimationENUM.EGG.value)
    
    # Update the pet every time animation has finished
    pet_object.updatePet(time_object.getTimePassed())
    
    print(pet_object.evolutionLvl)
    print(pet_object.getAge(time_object.getTimePassed()))
    
    
    
# Methods for threading
# Loop Animation Method for Thread
def displayCurrentAnimation():
    # Screen Loop for Animation Thread
    while pet_object.isAlive == True:
        # If the display == pet display then display animation
        if screen_object.getCurrentIndex() == 1:
            animation_object.startAnimation(pet_object.getCurrentAnimation())
            
            # Update the pet every time animation has finished
            pet_object.updatePet(time_object.getTimePassed())
            
            print(pet_object.evolutionLvl)
            print(pet_object.getAge(time_object.getTimePassed()))
        
        # If the display != pet display then display appropriate status
        if screen_object.getCurrentIndex() != 1:
            # Get the current screen index and use the animation class to display screen
            animation_object.screenAnimation(screen_object.getCurrentIndex(), pet_object, pet_object.getAge(time_object.getTimePassed()), light_object)
            animation_object.display.fill(0)
    
# Loop Touch Sensor Method for Thread
def touchListener():
    while True:
        status = touchSensor.read()
        
        # reference currentScreenIndex as a global variable
        #global currentScreenIndex
        
        if status[1]:
            # go left on display
            screen_object.goLeft(screen_object.getCurrentIndex())
            print("Current Screen Displayed: " + screen_object.screenArray[screen_object.getCurrentIndex()][0])
        if status[2]:
            # select action
            screen_object.doAction(screen_object.getCurrentIndex())
        if status[3]:
            # go right on display
            screen_object.goRight(screen_object.getCurrentIndex())
            print("Current Screen Displayed: " + screen_object.screenArray[screen_object.getCurrentIndex()][0])
            
        # Sleep delay in pressing action to stop spam
        sleep_ms(250)
    
    
# Condition for game starting after egg has hatched
while pet_object.evolutionLvl >= 1 and pet_object.isAlive == True:
    
    # Thread for OLED Animation
    t1 = threading.Thread(target=displayCurrentAnimation)
    # Thread for Touch Sensor
    t2 = threading.Thread(target=touchListener)
    # Start Threads and Join them
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    


