import paho.mqtt.publish as pb
from sys import stdout
from time import sleep
import requests
import RPi.GPIO as io
import time


io.setwarnings(False)

io.setmode(io.BOARD)

TRIG=3
ECHO=5

io.setup(TRIG,io.OUT)
io.setup(ECHO,io.IN)

i=0
def ultra():
         
        io.output(TRIG,False)
        sleep(0.2)

        io.output(TRIG,True)
        sleep(0.00001)

        io.output(TRIG,False)
        
            
        while io.input(ECHO)==0:
            pulse_start=time.time()
        

        while io.input(ECHO)==1:
            pulse_end=time.time()

        t=pulse_end-pulse_start

        d= t * 17150
        
        d= round(d, 2)

        print "d:",d,"cm"
        sleep(0.5)
        return str(d)

while True:
    c=ultra()
    
   
    pb.single("range",payload=str(c)+"cm",hostname="broker.shiftr.io",auth={'password':'8f9a04eeb2f2e524','username':'6391212a'})
    sleep(.1)
