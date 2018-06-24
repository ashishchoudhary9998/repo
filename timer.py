from datetime import datetime as dt
import sys


while True:
	hours   = str(dt.now().hour)
	minutes = str(dt.now().minute)
	seconds = str(dt.now().second)
	for_timer = hours + ":" + minutes + ":" + seconds
	sys.stdout.write('\r' + for_timer)
	sys.stdout.flush()

