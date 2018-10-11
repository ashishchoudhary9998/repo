import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
import paho.mqtt.publish as pb
from sys import stdout
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO_TRIGGER = 3
GPIO_ECHO = 7

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

i=0


def ultra():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

while True:
    ultra()
    pb.single("room1/temperature",payload=str(i),hostname="broker.shiftr.io",auth={'password':'8f9a04eeb2f2e524','username':'6391212a'})
    sleep(1)


    

