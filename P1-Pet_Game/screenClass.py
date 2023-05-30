"""
    Author: Ben Tegoni
    ID: 29728452
    Document: screenClass.py
    Description: Object for tracking display and screen animation indexes
"""

# Packages


# Time Class Object
class Screen:
    
    # Init Method + Instance Variables for Class
    def __init__(self):
        self.screenArray = [['info_screen'], ['pet_screen'], ['hunger_screen'], ['happiness_screen'], ['energy_screen'], ['sick_screen'], ['excretion_screen']]
        self.currentScreenIndex = 1

    # Methods / Functions
    def doAction(self, index):
        # get Current screen name
        currentScreenIndex = index
        if currentScreenIndex == 0:
            # no action
            print("Info No Action")
        if currentScreenIndex == 1:
            # no action
            print("Pet No Action")
        if currentScreenIndex == 2:
            # Feed Action
            print("Feed Action")
        if currentScreenIndex == 3:
            # Play Action
            print("Play Action")
        if currentScreenIndex == 4:
            # Lights Action
            print("Lights Action")
        if currentScreenIndex == 5:
            # Medicine Action
            print("Medicine Action")
        if currentScreenIndex == 6:
            # Clean Defecation
            print("Clean Defecation Action")
    
    # Method to go right on screen array
    def goRight(self, currentIndex):
        currentScreenIndex = currentIndex
        if currentScreenIndex == 6:
            self.currentScreenIndex = 0
        else:
            self.currentScreenIndex = currentScreenIndex + 1
    
    # Method to go left on screen array
    def goLeft(self, currentIndex):
        currentScreenIndex = currentIndex
        if currentScreenIndex == 0:
            self.currentScreenIndex = 6
        else:
            self.currentScreenIndex = currentScreenIndex - 1
    
    # Get Methods
    def getCurrentIndex(self):
        return self.currentScreenIndex
    
    # Set Methods
    
            
