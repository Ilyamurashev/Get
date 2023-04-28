import time, RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8 ,25, 24]


GPIO.setup (leds, GPIO.OUT)


for i in range (32):
    GPIO.output (leds[i%8], 1)
    time.sleep (0.2)
    GPIO.output (leds[i%8], 0)

GPIO.cleanup()