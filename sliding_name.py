import sys
from time import sleep


name = raw_input("Enter Names : ")
i = 0
j = 0
length = len(name)

while True:
	space = i + j
	space = space % (length + 1)
	sys.stdout.write(" "*space  + name[i] + " "*(length - space) + "\n")
	sys.stdout.flush()
	i = i + 1
	if i >= length:
		i = 0
		j = j + 1
		sys.stdout.write("\033[F"*(length))
		sys.stdout.write("\r"*(length))
		sys.stdout.flush()
	sleep(.012)
