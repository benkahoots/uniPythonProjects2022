import time
from PiicoDev_Unified import sleep_ms 

start = time.time()
sleep_ms(3000)

currentTime = time.time()
print(currentTime - start)
sleep_ms(3000)

currentTime = time.time()
print(currentTime - start)
