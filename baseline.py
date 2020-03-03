from sense_hat import SenseHat
from time import sleep
from random import randint


sense = SenseHat()
sense.set_rotation(180)

red = [255, 0, 0]  # Red
white = [255, 255, 255]  # White
blue= [0, 0 ,50]
purple = [225, 91, 243]
green = [141,255,92]
black= [0,0,0]
color=(randint(0,255), randint(0,255), randint(0,255) )


while True:
    #sense.show_message("Hello! We are New Media Development :)", text_colour=red, back_colour=white)
    sense.show_message("Hello! We are New Media Development :)", text_colour=white, back_colour=blue)
    sense.show_message("Hello! We are New Media Development :)", text_colour=black, back_colour=purple)
    sense.show_message("Hello! We are New Media Development :)", text_colour=color, back_colour=color)