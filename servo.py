import time
import RPi.GPIO as gpio

from utils import ultrasonic, servo

gpio.setmode(gpio.BCM)

(trig, echo) = (18, 24)
gpio.setup(21, gpio.OUT)

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

ultrasonic.initialize(trig)

servo.set_deg(21, 0)

while True:

    distance = 180 if int(ultrasonic.get_distance()) > 180 else int(ultrasonic.get_distance())
    
    print(f'Distance = {distance}')
    servo.set_deg(21, distance)

    time.sleep(0.3)