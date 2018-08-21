import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
from sys import stdout
from time import sleep
i = 0

person_to = raw_input("Enter person to contact : ")
person_from = raw_input("Enter your name : ")

while True:

	messageTo = raw_input(person_from + " : ")
	publish.single(person_from + "/" + person_to, messageTo, hostname="broker.shiftr.io",auth = {'username':"6391212a", 'password':"8f9a04eeb2f2e524'"})


	messageFrom = subscribe.simple(person_to + "/" + person_from, hostname="broker.shiftr.io",auth={'username':'6391212a', 'password':'8f9a04eeb2f2e524'})
	print messageFrom.payload
