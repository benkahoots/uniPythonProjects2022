import random
from PiicoDev_Unified import sleep_ms 

while True:
    sleep_ms(500)
    n = random.randint(1,2)
    print(n)
