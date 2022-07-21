import time
from RPi import GPIO as gpio

gpio.setmode(gpio.BCM)

gpio_list = [21, 20, 26, 19, 13, 22, 27, 17, 16, 12]

for p in gpio_list:
    gpio.setup(p, gpio.OUT)


gpio.output(21, True)
time.sleep(0.3)

for gp in gpio_list:
    
    gpio.output(gp, False)
    gpio.output(gp, True)
    
    time.sleep(0.3)
    
    gpio.output(gp, False)
    
for gp in gpio_list[::-1]:
    gpio.output(gp, False)
    gpio.output(gp, True)
    
    time.sleep(0.3)
    
    gpio.output(gp, False)
    
for gp in gpio_list:
    gpio.output(gp, True)
    time.sleep(0.3)
    
for gp in gpio_list[::-1]:
    gpio.output(gp, False)
    time.sleep(0.3)
    
for idx, gp in enumerate(gpio_list):
    gpio.output(gpio_list[idx - 1], True)
    gpio.output(gpio_list[-idx], True)
    time.sleep(0.3)  

for i in range(1, 5):
    gpio.output(gpio_list[5 - i], False)
    gpio.output(gpio_list[-6 + i], False)
    time.sleep(0.3)
    
gpio.output(gpio_list[9], False)

for i in range(0, 7):
    gpio.output(gpio_list[i], True)
    gpio.output(gpio_list[i + 2], True)
    time.sleep(0.3)
    gpio.output(gpio_list[i], False)
    gpio.output(gpio_list[i + 2], False)
    

gpio.output(gpio_list[7], True)
gpio.output(gpio_list[9], True)
time.sleep(0.3)
gpio.output(gpio_list[7], False)
gpio.output(gpio_list[9], False)

gpio.output(gpio_list[8], True)
time.sleep(0.3)
gpio.output(gpio_list[8], False)
time.sleep(0.3)
gpio.output(gpio_list[9], True)
time.sleep(0.3)
gpio.output(gpio_list[9], False)

for gp in gpio_list:
    
    gpio.output(gp, False)
    gpio.output(gp, True)
    
    time.sleep(0.3)
    
    gpio.output(gp, False)
    
for gp in gpio_list:
    
    gpio.output(gp, False)
    gpio.output(gp, True)
    
    time.sleep(0.3)
    
    gpio.output(gp, False)
    
cpy = gpio_list

for i in range(1, 10):

    for j in range(0, 11 - i):
        gpio.output(cpy[j], True)
        time.sleep(0.3)
        gpio.output(cpy[j], False)
    
    gpio.output(cpy[-i], True)
    
gpio.output(cpy[0], True)
    
for i in range(1, 5):
    gpio.output(gpio_list[5 - i], False)
    gpio.output(gpio_list[-6 + i], False)
    time.sleep(0.3)
    
gpio.output(gpio_list[9], False)
gpio.output(gpio_list[0], False)
        
exit()

