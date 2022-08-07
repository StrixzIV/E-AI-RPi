import time
import RPi.GPIO as gpio

from utils.ultrasonic import UltrasonicSensor

gpio.setmode(gpio.BCM)

(trig, echo) = (18, 24)
leds = [21, 20, 12, 5, 27]

ultrasonic_sensor = UltrasonicSensor(trig, echo)

for led in leds:
    gpio.setup(led, gpio.OUT)


while True:
    
    distance = ultrasonic_sensor.get_distance()
    print(f'Distance = {distance}')

    for led in leds:
        gpio.output(led, False)

    if 20 >= distance >= 5:

        print('5 to 20')
        
        for i in range(5):

            for led in leds:
                gpio.output(leds, True)
            
            time.sleep(0.3)

            for led in leds:
                gpio.output(leds, False)

            time.sleep(0.3)
    
    elif 50 >= distance > 21:

        print('21 to 50')

        for idx, gp in enumerate(leds):
            gpio.output(leds[idx - 1], True)
            gpio.output(leds[-idx], True)
            time.sleep(0.3)  

        for led in leds:
            gpio.output(led, False)


    elif 100 >= distance > 51:
        
        gpio.output(leds[0], True)
        gpio.output(leds[2], True)
        gpio.output(leds[4], True)

        gpio.output(leds[1], False)
        gpio.output(leds[3], False)

        time.sleep(0.3)
        
        gpio.output(leds[0], False)
        gpio.output(leds[2], False)
        gpio.output(leds[4], False)

        gpio.output(leds[1], True)
        gpio.output(leds[3], True)

    elif 150 >= distance > 101:

        print('101 to 150')

        for led in leds:
            gpio.output(led, True)

        for led in leds:
            time.sleep(0.3)
            gpio.output(led, False)

    elif distance > 150:
        print('150++')

    time.sleep(1)