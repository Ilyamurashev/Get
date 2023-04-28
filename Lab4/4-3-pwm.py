import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

pwm = GPIO.PWM(22, 60)
pwm.start(0)
try:
    while True:
        dc = int(input("Enter the duty cicle(0 < dc < 100)"))
        pwm.ChangeDutyCycle(dc)
finally:
    pwm.stop()
    GPIO.cleanup()