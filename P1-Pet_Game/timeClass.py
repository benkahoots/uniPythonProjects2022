"""
    Author: Ben Tegoni
    ID: 29728452
    Document: timeClass.py
    Description: Object for time of process running, to keep track of age.
"""

# Packages
import time

# Time Class Object
class Time:
    
    # Init Method + Instance Variables for Class
    def __init__(self):
        self.startTime = time.time()
        self.endTime = None # When game ends calculate the end time/death age
        self.currentTime = None
        
    # Get Methods
    def getTimePassed(self):
        self.currentTime = time.time()
        timePassed = self.currentTime - self.startTime
        currentAge = ("%.0f" % timePassed)
        return currentAge
    
    # Set Methods
