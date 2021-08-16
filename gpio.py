# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# 1  BOARD=35
# 2  BOARD=33


def duoji(pin, angle):
    angle=angle*2
    GPIO.setup(pin, GPIO.OUT)
    p = GPIO.PWM(pin, 50)
    p.start(0)
    time.sleep(1)
    for i in range(0, angle, 5):
        p.ChangeDutyCycle(2.5+10.0*i/angle)
        time.sleep(0.1)
    GPIO.cleanup()


duoji(33, 360)
