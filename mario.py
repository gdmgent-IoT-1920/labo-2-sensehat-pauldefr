from sense_hat import SenseHat
import time


sense = SenseHat()
sense.set_rotation(180)

sense.clear()

X = [255, 0, 0]  # Red
S = [255, 204, 102] #Skin
B = [0, 120, 255] #Blue
O = [50, 50, 50]  # White

mario = [
O, O, O, O, O, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, S, S, O, O, O,
O, O, X, B, B, O, O, S,
O, S, O, B, B, B, X, O,
O, O, O, B, B, B, O, O,
O, O, B, O, O, B, O, O,
O, O, S, O, O, S, O, O
]

marioJump = [
O, O, O, S, S, O, O, O,
O, O, X, B, O, O, O, O,
O, S, O, B, X, S, O, O,
O, O, O, B, O, O, O, O,
O, O, O, B, B, O, O, O,
O, O, B, O, B, O, O, O,
O, O, S, O, S, O, O, O,
O, O, O, O, O, O, O, O

]
sense.set_pixels(mario)


while('true'):
    event = sense.stick.wait_for_event()
    
    if event.direction == 'up':
        sense.clear()
        sense.set_pixels(marioJump)
        time.sleep(0.5)
        sense.set_pixels(mario)