from collections import Counter

# Problem taken from r/beginnerprojects
# Code written by SnoozeSecurity (youtube.com/channel/UCa5QaVWjwFkUNoLtMka1d3w)

# Mean function

def mean(list):
        sum = 0
        for i in range(len(list)):
                sum = sum + list[i]
        mean = sum / counter
        print 'Mean: ', mean

# Median function takes list of numbers, sorts from least to greatest, calculates median(s)

def med(list):
	list.sort()
	if len(list) % 2 != 0:
		print 'Median: ', (list[(len(list) / 2)])
	else:
		print 'Medians: ', (list[(len(list) / 2) - 1], list[(len(list) / 2)])

# Mode function (currently only shows one mode, needs work)

def mode(list):
	d = max(set(list), key=list.count)
	print 'Mode: ', d

listNum = []
counter = 0

# Gets list of numbers from user and quits at non-integer entry

while True:
        numStr = raw_input('Enter a number to be added to a list; Q to calculate; any non-number to quit: ')
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

mean(listNum)
med(listNum)
mode(listNum)