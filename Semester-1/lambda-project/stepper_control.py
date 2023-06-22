import time
import RPi.GPIO as gpio

control_pin = [5, 6, 13, 19]
control_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

def setup() -> None:

    '''
        Setup stepper motor gpio
    '''

    for pin in control_pin:
        gpio.setup(pin, gpio.OUT)
        gpio.output(pin, False)


def forward() -> None:

    '''
        Drive 1 step forward
    '''
    
    for half_step in range(8):
        for pin in range(4):
            gpio.output(control_pin[pin], control_sequence[half_step][pin])

        time.sleep(0.001)


def backward() -> None:

    '''
        Drive 1 step backward
    '''
    
    for half_step in range(8):
        for pin in range(4):
            gpio.output(control_pin[pin], control_sequence[::-1][half_step][pin])

        time.sleep(0.001)


