import RPi.GPIO as gpio
from time import sleep


dac = [26, 19, 13,6,5,11,9,10]
comp = 4
troyka = 17
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka , gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def dec2bin(a, n):
    return [int (i) for i in bin(a)[2:].zfill(n)]

def adc():
    for i in range(256):
        dac_curr = dec2bin(i, 8)
        gpio.output(dac, dac_curr)
        compvalue = gpio.input(comp)
        sleep(0.01)
        if (compvalue == 0):
            return i

try: 
    while True:
        k = adc()
        voltage = 3.3*k/256
        if (voltage != 0):
            print("Цифровое значение: ",k ,", соответствующее напряжение: ", voltage,"V")
            
finally:
    gpio.output(dac, 0)
    gpio.cleanup()



