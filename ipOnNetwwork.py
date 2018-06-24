#from os import system
from subprocess import check_output
import argparse
import sys

# construct th argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True,help="enter ip address.")
ap.add_argument("-n","--name",required=False)
args = vars(ap.parse_args())
print args

ip = args['ip']

command = 'ping ip -c 1 -w 1 -b'
command_in_list = command.split(' ')
for i in range(255):
	#print "_"*50
	try:
		command = 'ping -c 1 -w 1 -b %s.%s' % (ip,str(i))
		sys.stdout.write('\r'+ ip + "." + str(i))
		sys.stdout.flush()
		command_in_list = command.split(' ')

		output = check_output(command_in_list)
		if output.find("1 received") > -1:
			#print "#"*50
			sys.stdout.write('\r')
			sys.stdout.flush()
			print ip + "." + str(i), "is online."
			#print "#"*50
	except Exception as ex:
		pass
		#print ip,"\r",
		#print "Exception is : ", ex.output
print "End"
