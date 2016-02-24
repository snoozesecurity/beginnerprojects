# Problem taken from r/beginnerprojects
# Code written by SnoozeSecurity (youtube.com/channel/UCa5QaVWjwFkUNoLtMka1d3w)

# Mean function

import sys

def mean(listNum, toFormat):
	sum = 0
	for i in range(len(listNum)):
		sum = sum + listNum[i]
	mean = sum / counter
	print 'Mean: ', round(mean, toFormat)

# Median function takes listNum of numbers, sorts from least to greatest, calculates median(s)

def med(listNum):
	if len(listNum) % 2 != 0:
		print 'Median: ', (listNum[(len(listNum) / 2)])
	else:
		print 'Medians: ', ((listNum[(len(listNum) / 2) - 1] +  listNum[(len(listNum) / 2)]) / 2)

# Mode function takes listNum of numbers, creates a 2D list based on unique numbers in listNum, and increments count for each in the second dimension

def mode(listNum):
	mySet = set(listNum)
	mySetList = list(mySet)
		
	largestIndex = float("-inf") # Initializes largestIndex with a value of negative infinity
	largestNumber = float("-inf") # Ditto but for a number rather than an index
	
	# MySeenList is 2D array as mentioned above
	
	mySeenList = [[0, 0] for x in range(len(mySetList))]
	for i in range(len(mySeenList)):
		mySeenList[i][0] = mySetList[i]
		mySeenList[i][1] = listNum.count(mySetList[i])
		if (largestNumber < listNum.count(mySetList[i])):
			largestIndex = i
			largestNumber = listNum.count(mySetList[i])
			
	
	modes = [] # Intializes empty list of modes; we then add modes to the list by looking for largestNumber in the second dimension of MySeenList
	
	for i in range(len(mySeenList)):
		if mySeenList[i][1] == largestNumber:
			modes.append(mySeenList[i])
			
	# Determines number of modes and prints accordingly
			
	if len(modes) > 1:
		for i in range(len(modes)):
			print "Mode", i + 1, ": ", modes[i][0], " with ", modes[i][1], " occurrences."
	else:
		for i in range(len(modes)):
			print "Mode:", modes[i][0], "with", modes[i][1], "occurrences."

listNum = []
counter = 0
			
# Gets listNum of numbers from user and quits at non-integer entry

while True:
        numStr = raw_input('Enter a number to be added to a listNum; Q to calculate; any non-number to quit: ')
        if counter > 0 and numStr.lower() == 'q':
                print 'Calculating...'
                break
        try:
                num = float(numStr)
        except (TypeError, ValueError):
                print 'Goodbye!'
                break
        listNum.append(num)
        counter += 1

listNum.sort()

# Asks user how many decimals the mean should be rounded to; quits program on illegal entry

toFormat = 0
preFormat = raw_input("How many decimals to round for the mean?")
try:
	toFormat = int(preFormat)
except (TypeError, ValueError, NameError):
	print 'Goodbye!'
	sys.exit(1)

# Calls functions to perform calculations	
	
mean(listNum, toFormat)
med(listNum)
mode(listNum)