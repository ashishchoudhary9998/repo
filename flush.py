import sys
from time import sleep

name = raw_input("Enter Names : ")
i = 0
j = 0
length = len(name)

while True:
	space = i
	if ( j % length ) < i:
		sys.stdout.write("\n"*(j % length))
	sys.stdout.write(" "*space  + name[i] + " "*(length - space) + "\n")
	i = i + 1
	if i >= length:
		i = 0
		j = j + 1
		sys.stdout.write("\033[F"*(length))
		sys.stdout.write("\r"*(length))
		sys.stdout.flush()
	sleep(.005)
