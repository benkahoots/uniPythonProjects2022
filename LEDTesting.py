from PiicoDev_RGB import PiicoDev_RGB, wheel
from PiicoDev_Unified import sleep_ms # Cross-platform compatible sleep function


healthLED1 = PiicoDev_RGB(id=[0,0,0,0]) # initialise the LED module with conservative default brightness
healthLED2 = PiicoDev_RGB(id=[1,0,0,0])
# leds.setBrightness(127) # 0-255 set the global brightness to half

# pre-define some colours
red = [255,0,0] 
green = [0,255,0]
blue = [0,0,255]
yellow = [255,255,0]
magenta = [255,0,255]
cyan = [0,255,255]
white = [255,255,255]
black = [0,0,0]

# Example 1: Set LEDs to pure Red, Green, Blue for 3 seconds
healthLED1.setPixel(0, green)
healthLED1.setPixel(1, green)
healthLED1.setPixel(2, red)
healthLED1.show() # call show() to update the LEDs with new colours
#sleep_ms(1000)
#leds.clear() # clear the LEDs

healthLED2.setPixel(0, red)
healthLED2.setPixel(1, red)
healthLED2.setPixel(2, red)
healthLED2.show()
#sleep_ms(1000)
#leds2.clear() # clear the LEDs



# Example 2

# i = 0 # loop counter
# powerLedState = True
# 
# while True:
#     c = wheel(i/360) # pick a colour from the colour wheel
#     leds.fill(c) # fill() will automatically show()
#     
#     if i % 100 == 0: # every 100 loops toggle the power LED
#         powerLedState = not powerLedState # toggle state variable
#         leds.pwrLED(powerLedState) # update power LED       
#     
#     i = i+1
#     sleep_ms(5)