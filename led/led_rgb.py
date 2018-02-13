#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GREEN = 33
YELLOW = 35
RED = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)

try:
	for i in range(0,1):
		t = 1
		if t==1:
			GPIO.output(RED,False)
			GPIO.output(YELLOW,False)
			GPIO.output(GREEN,True)
			time.sleep(2)
			t=2
		if t==2:
			GPIO.output(RED,True)
			GPIO.output(YELLOW,False)
			GPIO.output(GREEN,False)
			time.sleep(2)
			t=3
		if t==3:
			GPIO.output(RED,False)
			GPIO.output(YELLOW,True)
			GPIO.output(GREEN,False)
			time.sleep(1)
			t=1
        GPIO.cleanup()

except KeyboardInterrupt:
	pass

