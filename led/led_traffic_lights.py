import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.output(18,GPIO.LOW)
GPIO.output(4,GPIO.LOW)
GPIO.output(25,GPIO.LOW)

while True:
    GPIO.output(18,GPIO.HIGH)
    time.sleep(30)
    GPIO.output(18,GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(18,GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(4,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(4,GPIO.LOW)
    GPIO.output(25,GPIO.HIGH)
    time.sleep(30)
    GPIO.output(25,GPIO.LOW)


GIPO.cleanup()

