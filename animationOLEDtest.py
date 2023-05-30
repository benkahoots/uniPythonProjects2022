# Display a portable bitmap image (.pbm)
from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

display = create_PiicoDev_SSD1306()


while True:
    display.load_pbm('GIF_test/egg-frame-1.pbm', 1)
    display.show()
    sleep_ms(500)
    display.fill(0)
    
    display.load_pbm('GIF_test/egg-frame-2.pbm', 1)
    display.show()
    sleep_ms(500)
    display.fill(0)