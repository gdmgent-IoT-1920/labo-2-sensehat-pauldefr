from sense_hat import SenseHat
import time
from random import randint

sense=SenseHat()
sense.clear()

keys = ['N','M','D']

while True:
    for key in keys:
        color=(randint(0,255), randint(0,255), randint(0,255) )
        sense.show_letter(key, text_colour=color)
        time.sleep(0.5)
    time.sleep(2)