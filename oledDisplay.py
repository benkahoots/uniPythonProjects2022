from PiicoDev_SSD1306 import *
display = create_PiicoDev_SSD1306()

myString = "this is me"
myNumber = 29728452

display.text("Hello, Tegoni!", 0,0, 1) # literal string
display.text(myString, 0,15, 1) # string variable
display.text(str(myNumber), 0,30, 1) # print a variable
display.show()