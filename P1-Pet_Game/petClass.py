"""
    Author: Ben Tegoni
    ID: 29728452
    Document: petClass.py
    Description: Object for main character/pet
"""

# Packages
from PiicoDev_Unified import sleep_ms
import random

# Class/Object Imports
from timeClass import Time
from animationClass import *

# Time Class Object
class Pet:
    
    # Init Method + Instance Variables for Class
    def __init__(self, timePassed_):
        # Initialised Pet Information
        self.isAlive = True
        self.age = timePassed_ # From timeClass.py
        self.gender = self.setGender() # 1 = Male, 2 = Female
        self.evolutionLvl = 0 # 0 = Egg, 1 = Baby, 2 = Teen, 3 = Adult, 4 = Old
        self.weight = "1.8kg"
        self.isAsleep = False
        self.currentAnimation = AnimationENUM.EGG.value
        
        # Intialised Stats
        self.happinessStatus = 3.000 # Max: 6.000 - Most Happy
        self.hungerStatus = 3.000 # Max: 6.000 - Most Hungry
        self.energyStatus = 6.000 # Max: 6.000 - Most Energy
        self.sickStatus = 0.000 # Max: 6.000 - Most Sick
        self.excretionStatus = 1.000 # Max: 6.000 - Will Poo.
        
        
    # Get Methods
    def getAliveStatus(self):
        return self.isAlive
    
    def getAge(self, timePassed_):
        self.age = timePassed_
        currentAge = ("Age: " + self.age + " Days")
        return currentAge
    
    def getWeight(self):
        return self.weight
    
    def getEvolution(self):
        return self.evolutionLvl
    
    def getExcretion(self):
        return self.excretionStatus
    
    def getSick(self):
        return self.sickStatus
    
    def getEnergy(self):
        return self.energyStatus
    
    def getHappiness(self):
        return self.happinessStatus
    
    def getHunger(self):
        return self.hungerStatus
    
    
    
    def getCurrentAnimation(self):
        return self.currentAnimation
    
    # Set Methods
    def setGender(self):
        n = random.randint(1,2)
        if n == 1:
            return "Male"
        else:
            return "Female"
        
    # Functions/Methods
    # Updates a Pets Entire Data Registry and all Statistics Surrounding it.
    def updatePet(self, timePassed_):
        # Get the age of the pet
        age = timePassed_
        
        # Check the evolution is up-to-date
        self.checkEvolveStatus(age)
    
    # Checks to see if a pet can evolve
    def checkEvolveStatus(self, age_):
        # get the current age
        age = age_
        
        # Evolution 0 to 1 logic (Egg to Hatch) 5 min normally but for testing itll be 10 seconds
        if(self.evolutionLvl == 0 and int(age) == 1):
            # Upgrade Evolution Level
            self.evolutionLvl = 1
            # Set current Idle animation
            self.currentAnimation = AnimationENUM.EVOL_1_IDLE.value
            # Play The Egg_Hatch Animation
            tempAnimation = Animation()
            tempAnimation.startAnimation(AnimationENUM.EGG_HATCH.value)
            
            
            
            
        
    
