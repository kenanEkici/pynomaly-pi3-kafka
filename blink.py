import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)

def blink():
    while True:
        GPIO.output(8, GPIO.HIGH)
        sleep(1/4)
        GPIO.output(8, GPIO.LOW)
        sleep(1/4)

def off():
    GPIO.output(8,GPIO.LOW)
