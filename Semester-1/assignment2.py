import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

btns = [27, 6]
leds = [5, 13, 26, 19, 21]
led_counter = 0

for btn in btns:
    gpio.setup(btn, gpio.IN, pull_up_down = gpio.PUD_UP)
    
for led in leds:
    gpio.setup(led, gpio.OUT)
    

while True:
    
    state1 = gpio.input(btns[0]) != 1
    state2 = gpio.input(btns[1]) != 1
    
    print(f'Btn1: {state1}, Btn2: {state2}')
    
    if state1 and state2:
        for led in leds:
            gpio.output(led, False)
            
        led_counter = 0
                     
    elif state1:
        
        if led_counter == 5:
            gpio.output(leds[4], False)
            led_counter = 0
                     
        else:
            
            for led in leds:
                gpio.output(led, False)
                
            gpio.output(leds[led_counter], True)
            led_counter += 1
            
    elif state2:
        
        for led in leds:
            gpio.output(led, False)
            
        for i in range(5):
            gpio.output(leds[i], True)
            time.sleep(0.3)
            gpio.output(leds[i], False)
            time.sleep(0.3)
    
    time.sleep(0.3)