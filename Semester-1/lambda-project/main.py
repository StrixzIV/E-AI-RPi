import cv2
import time

import numpy as np
import RPi.GPIO as gpio

import stepper_control

gpio.setmode(gpio.BCM)
cam_stream = cv2.VideoCapture(0)

btns = (16, 20, 21)

for btn in btns:
    gpio.setup(btn, gpio.IN, pull_up_down = gpio.PUD_UP)

stepper_control.setup()

while True:

    state1 = not bool(gpio.input(btns[0]))
    state2 = not bool(gpio.input(btns[1]))
    state3 = not bool(gpio.input(btns[2]))

    if state1 and not state2 and not state3:
        stepper_control.forward()

    elif state2 and not state1 and not state3:
        stepper_control.backward()

    elif state3 and not state1 and not state2:
        (has_frame, frame) = cam_stream.read()
        
        if not has_frame:
            continue

        cv2.imwrite('a.png', frame)
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (_, res)  = cv2.threshold(gray, 78, 255, cv2.THRESH_BINARY)
        
        (contours, _) = cv2.findContours(res, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
        print('Mesuring antinode...')
        print(f'detected: n = {len(contours)}')

        cv2.imwrite('out.png', res)

cam_stream.release()
cv2.destroyAllWindows()
