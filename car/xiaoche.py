#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import time

#按物理排线方式
GPIO.setmode(GPIO.BOARD)

#另一面
INT0 = 29
INT1 = 31
INT2 = 32

#一面
INT3 = 33
INT4 = 35
INT5 = 37

GPIO.setup(INT0,GPIO.OUT)
GPIO.setup(INT1,GPIO.OUT)
GPIO.setup(INT2,GPIO.OUT)

GPIO.setup(INT3,GPIO.OUT)
GPIO.setup(INT4,GPIO.OUT)
GPIO.setup(INT5,GPIO.OUT)

pwm1 = GPIO.PWM(INT0,80)
pwm1.start(90)
pwm2 = GPIO.PWM(INT5,80)
pwm2.start(90)

#HIGH高电平的时候是正传，LOW低电平的时候是反转
GPIO.output(INT0,GPIO.HIGH)
GPIO.output(INT1,GPIO.HIGH)
GPIO.output(INT2,GPIO.LOW)
GPIO.output(INT3,GPIO.HIGH)
GPIO.output(INT4,GPIO.LOW)
GPIO.output(INT5,GPIO.HIGH)

for num in range(0,5):
    pwm1.ChangeDutyCycle(90)
    pwm2.ChangeDutyCycle(90)
    time.sleep(3)
    pwm1.ChangeDutyCycle(30)
    pwm2.ChangeDutyCycle(30)
    time.sleep(3)

time.sleep(2)

GPIO.cleanup()

