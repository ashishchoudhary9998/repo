import RPi.GPIO as GPIO
import time, sys
GPIO.setwarnings(False)


led=3

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(led,GPIO.OUT)

global count
count = 0
c=" "


def countPulse(channel):
   global count
   if start_counter == 1:
      count = count+1
      print count
      flow = count / (60 * 7.5)
      print(flow)
      

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)


c=int(
   input("enter water level"))   
   
while True:
       
    
    try:
        start_counter = 1
        time.sleep(1)
        start_counter = 0
        flow = (count * 60 * 2.25 / 1000)
        
        print "The flow is: %.3f Liter/min" % (flow)
        
        time.sleep(1)
        
        
        if(c<flow):
           GPIO.output(led,GPIO.LOW)
           print 'led off'   
           time.sleep(1)

        elif(c>=flow):
           GPIO.output(led,GPIO.HIGH)
           print 'led on'
           time.sleep(1)


    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()