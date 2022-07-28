import time
import RPi.GPIO as gpio

def initialize(trig_pin: int) -> None:
    
    '''
        Initializing ultrasonic sensor before running.
    '''
    
    print('Starting...')
    
    gpio.output(trig_pin, False)
    print('Wait for sensor...')
    
    time.sleep(1)


def get_distance(trig_pin: int, echo_pin: int) -> float:
    
    '''
        Get distance from ultrasonic sensor.
    '''
    
    gpio.output(trig_pin, True)
    time.sleep(0.00001)
    gpio.output(trig_pin, False)

    start_pulse = time.time()
    end_pulse = time.time()

    while gpio.input(echo_pin) == 0:
        start_pulse = time.time()

    while gpio.input(echo_pin) == 1:
        end_pulse = time.time()

    duration = end_pulse - start_pulse
    distance = abs(round((duration * 17150), 2))

    return distance