import RPi.GPIO as g
import time
from time import sleep
g.setmode(g.BOARD)
g.setwarnings(False)
g.setup(3,g.OUT)
g.setup(5,g.OUT)
g.setup(7,g.OUT)
g.setup(8,g.OUT)

def pattern():    
#For led on one by one
    g.output(3,1)
    time.sleep(1)
    g.output(5,1)
    time.sleep(1)
    g.output(7,1)
    time.sleep(1)
    g.output(8,1)
    time.sleep(1)

print 'led on'
#For led off one by one
def pattern2():
    g.output(3,0)
    time.sleep(1)
    g.output(5,0)
    time.sleep(1)
    g.output(7,0)
    time.sleep(1)
    g.output(8,0)
    time.sleep(1)

print 'led off'    
while True:

    pattern()
    time.sleep(1)
    pattern2()
    time.sleep(1)    




