import RPi.GPIO as gpio

def belt_start(in1: int, in2: int) -> None:
    
    '''
        Start the belt motor in forward direction.
    '''
    
    gpio.output(in1, gpio.LOW)
    gpio.output(in2, gpio.HIGH)


def belt_stop(in1: int, in2: int) -> None:
    
    '''
        Stop the belt motor from moving.
    '''
    
    gpio.output(in1, gpio.LOW)
    gpio.output(in2, gpio.LOW)
    

def belt_reverse(in1: int, in2: int) -> None:
    
    '''
        Start the belt motor in reverse direction.
    '''
    
    gpio.output(in1, gpio.HIGH)
    gpio.output(in2, gpio.LOW)