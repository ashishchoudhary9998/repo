import RPi.GPIO as io
import time
from time import sleep
import picamera


io.setwarnings(False)

io.setmode(io.BOARD)

IR_INPUT = 3

io.setup(IR_INPUT,io.IN)





def cam():
    #create object for PiCamera class
    camera = picamera.PiCamera()
    #set resolution
    camera.resolution = (1024, 768)
    camera.brightness = 60
    camera.start_preview()
    #add text on image
    camera.annotate_text = 'Hi Pi User'
    sleep(1)
    #store image
    camera.capture('image3.jpeg')
    camera.stop_preview()

while True:
    
    c = io.input(IR_INPUT)
    if(c==1):
        
        cam()
        print "on"      
                 
    elif(c==0):
        
        print "off"