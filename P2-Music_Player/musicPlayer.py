# Sound Testing
from audioplayer import AudioPlayer

# Reading Files from a Directory
import os

# Read the touch sensor buttons and print the result
from PiicoDev_CAP1203 import PiicoDev_CAP1203
from PiicoDev_Unified import sleep_ms # cross-platform-compatible sleep

#OLED Display Import Package
from PiicoDev_SSD1306 import *

# Global Song Data Array
musicDetailsArray = [[],[]]

# Function for listing all files within a system directory
def getFiles():
    # Get all files in the directory
    file_list = os.listdir('music-files/.')
    # Get all items in directory array and sperate the artist and song name
    i = 0
    for song in file_list:
        tempSplit = song.split(' - ')
        # set artist variable
        artistStr = tempSplit[0]
        # set song name variable
        songStr = tempSplit[1].split('.')
        songStr = songStr[0]
        # Append Song and Artist Details to Music Array
        musicDetailsArray[0].append([artistStr, songStr])
        musicDetailsArray[1].append([song])
        
def displayData():
    # Create the display using the PiicoDev Library
    display = create_PiicoDev_SSD1306()
    # Set the Current Song Artist Name
    artistNameStr = musicDetailsArray[0][songIndex][0]
    # Set the Current Song Title Name
    songTitleStr = musicDetailsArray[0][songIndex][1]
    # Get the length of the song title
    songTitleLen = len(songTitleStr)
    # if the title needs 1 line to display
    if songTitleLen <= 13:
        display.text(songTitleStr, 0,20, 1)
        # check to see if song playing data needs to display
        if songPlaying == True:
            display.text("Playing", 0, 50, 1)
        else:
            display.text("Paused", 0, 50, 1)
    # If the title length needs to lines to display
    elif songTitleLen > 13 and songTitleLen < 27:
        firstLine = (songTitleStr[0:14] + "..")
        secondLine = (".." + songTitleStr[14:songTitleLen])
        display.text(firstLine, 0, 20, 1)
        display.text(secondLine, 0, 30, 1)
        # check to see if song playing data needs to display
        if songPlaying == True:
            display.text("Playing", 0, 50, 1)
        else:
            display.text("Paused", 0, 50, 1)
    # Display Artist Info on SCreen
    display.text(artistNameStr, 0,0, 1)
    # Display Text to Screen
    display.show()

# Run the getFiles() function to sort all data into array format
getFiles()
# Allow for one button at a time with minimum sensitivity to avoid double clicking
touchSensor = PiicoDev_CAP1203(touchmode="single", sensitivity=6)
# When Starting the application, set the song to be playing   
songPlaying = True
# When starting the application setup initial song index
songIndex = 1

# Start playing an initial song on application open
currentSong = AudioPlayer("music-files/" + musicDetailsArray[1][songIndex][0])
currentSong.play(loop=False, block=False)
displayData()

# Open a never ending loop to play music
while True:
    # Example: Display touch-pad statuses
    status = touchSensor.read()
    # print("Touch Pad Status: " + str(status[1]) + "  " + str(status[2]) + "  " + str(status[3]))
    
    # Play/Pause Button Functionality
    if status[2]:
        #AudioPlayer("convertMP3.mp3").play(block=True)
        if songPlaying == True:
            songPlaying = False
            currentSong.pause()
            # Refresh Display with new info
            displayData()
            print(str(musicDetailsArray[0][songIndex]) + " ... has been paused.")
        elif songPlaying == False:
            songPlaying = True
            currentSong.resume()
            # Refresh Display with new info
            displayData()
            print(str(musicDetailsArray[0][songIndex]) + " ... has begun playing.")
            
    # Rewind Button Functionality
    if status[1]:
        currentSong.play(loop=False, block=False)
        # Change Song Playing Status
        songPlaying = True
        # Refresh Display with new info
        displayData()
        print(str(musicDetailsArray[0][songIndex]) + " has restarted.")
    
    # Fast-Forward Button Functionality
    if status[3]:
        # If the playlist ended, check and loop the songs
        if songIndex == len(musicDetailsArray[0]) - 1:
            songIndex = 0
            print("The next song playing is ... " + str(musicDetailsArray[0][songIndex]) + " ... " + str(musicDetailsArray[1][songIndex]))
            currentSong = AudioPlayer("music-files/" + musicDetailsArray[1][songIndex][0])
            currentSong.play(loop=False, block=False)
            # Change Song Playing Status
            songPlaying = True
            # Refresh Display with new info
            displayData()
        else:
            print("The next song playing is ... " + str(musicDetailsArray[0][songIndex+1]) + " ... " + str(musicDetailsArray[1][songIndex+1]))
            currentSong = AudioPlayer("music-files/" + musicDetailsArray[1][songIndex+1][0])
            currentSong.play(loop=False, block=False)
            # Update Current index of song
            songIndex += 1
            # Change Song Playing Status
            songPlaying = True
            # Refresh Display with new info
            displayData()
    # Sleep delay in pressing action to stop spam
    sleep_ms(250)