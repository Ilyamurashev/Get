import time, RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11 ,9, 10]
GPIO.setup (dac, GPIO.OUT)

number = [0, 1, 1, 1, 1, 1, 1, 1]

GPIO.output(dac, number) 


for i in range (8):
    GPIO.output(dac[i], number[i])
time.sleep (10)

GPIO.output(dac, 0)
GPIO.cleanup()