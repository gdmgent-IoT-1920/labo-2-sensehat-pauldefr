from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()
sense.clear()

while True:
    c=(randint(0,255),randint(0,255),randint(0,255))
    b=(0,0,0) #blank

    rectangle1 = [
        c,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
    ]
    rectangle2 = [
        c,c,c,c,b,b,b,b,
        c,b,b,c,b,b,b,b,
        c,b,b,c,b,b,b,b,
        c,c,c,c,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
    ]
    rectangle3 = [
        c,c,c,c,c,c,b,b,
        c,b,b,b,b,c,b,b,
        c,b,b,b,b,c,b,b,
        c,b,b,b,b,c,b,b,
        c,b,b,b,b,c,b,b,
        c,c,c,c,c,c,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
    ]
    rectangle4 = [
        c,c,c,c,c,c,c,c,
        c,b,b,b,b,b,b,c,
        c,b,b,b,b,b,b,c,
        c,b,b,b,b,b,b,c,
        c,b,b,b,b,b,b,c,
        c,b,b,b,b,b,b,c,
        c,b,b,b,b,b,b,c,
        c,c,c,c,c,c,c,c,
    ]


    sense.set_pixels(rectangle1)
    time.sleep(0.5)
    sense.set_pixels(rectangle2)
    time.sleep(0.5)
    sense.set_pixels(rectangle3)
    time.sleep(0.5)
    sense.set_pixels(rectangle4)
    time.sleep(0.5)
    sense.set_pixels(rectangle3)
    time.sleep(0.5)
    sense.set_pixels(rectangle2)
    time.sleep(0.5)