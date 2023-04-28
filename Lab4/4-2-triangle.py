import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
k = 0
GPIO.setup(dac, GPIO.OUT)
def convert_dec_to_bin(x):
    return bin(x)[2:].zfill(8)

try:
    while k < 1
        j = int(input())
        for n in range(256):
            print("expected: ", round(n / 255*3.3128,2))
            b = [int(i) for i in list(convert_dec_to_bin(int(n)))]
            GPIO.output(dac,b)
            time.sleep(j/512)
        for n in range(255,1,-1):
            print("expected: ", round(n / 255*3.3128,2))
            b = [int(i) for i in list(convert_dec_to_bin(int(n)))]
            GPIO.output(dac,b)
            time.sleep(j/512)
        k = k+1

except Exception as e:
    print("Error ",e)

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()