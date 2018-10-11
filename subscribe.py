import paho.mqtt.subscribe as subscribe
from sys import stdout
from time import sleep

while True:
     msg=subscribe.simple("room1/temperature",hostname="broker.shiftr.io",auth={'password':'8f9a04eeb2f2e524','username':'6391212a'})
     print msg.payload
     sleep(0.01)

     msg=subscribe.simple("room2/temperature",hostname="broker.shiftr.io",auth={'password':'8f9a04eeb2f2e524','username':'6391212a'})
     print msg.payload
     sleep(0.01)

     msg=subscribe.simple("room3/temperature",hostname="broker.shiftr.io",auth={'password':'8f9a04eeb2f2e524','username':'6391212a'})
     print msg.payload
     sleep(0.01)

     
