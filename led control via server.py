import requests
import RPi.GPIO as io
import time
from time import sleep

io.setwarnings(False)

io.setmode(io.BOARD)

io.setup(3,io.OUT)
led=3

while True:

        data = requests.get("http://class.aarmontech.com/3/bulb.txt")
        print data.text
                        
                
        if (data.text=="1"):
          
          io.output(led,True)      
          print 'led on'
          time.sleep(1)

        elif (data.text=="0"):
          
         io.output(led,False)       
         time.sleep(1)
         print 'led off'