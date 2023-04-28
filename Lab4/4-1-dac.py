import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def convert_dec_to_bin(x):
    return bin(x)[2:].zfill(8)

try:
    while True:
        n = input()
        if (n == "q"):
            print("Goodbuy")
            break
        if (not(n.isdigit())):
            print("error")
            continue
        try:
            n = int(n)
        except ValueError():
            print("error")
            continue
        if (n < 0):
            print("error")
            continue
        if (n > 255):
            print("error")
            continue
        
        b = [int(i) for i in list(convert_dec_to_bin(int(n)))]
        GPIO.output(dac,b)

except Exception as e:
    print("Error ",e)

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()