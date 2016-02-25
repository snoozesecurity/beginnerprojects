# Problem taken from r/beginnerprojects
# Code written by SnoozeSecurity (youtube.com/channel/UCa5QaVWjwFkUNoLtMka1d3w)

import sys

num1 = 0
num2 = 1
fibOut = 0

numSequence = int(input("How many numbers into the Fibonacci Sequence? "))
if (numSequence < 1): # Checks input; quits if illegal
	print "Invalid input!"
	sys.exit(1)

# Performs calculations and keeps track of output in fibOut
	
for i in range(numSequence):
	if i == 0:
		fibOut = 0
		print fibOut
	elif i == 1:
		fibOut = 1
		print fibOut
	else:
		fibOut = num1+num2
		num1 = num2
		num2 = fibOut
		print fibOut