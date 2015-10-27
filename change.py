# Problem taken from r/beginnerprojects
# Code written by SnoozeSecurity (youtube.com/channel/UCa5QaVWjwFkUNoLtMka1d3w)
# I am not a professional programmer, rather someone trying to learn python!

import time
import math

# Setting coin values

quarter = .25
dime = .10
nickel = .05
penny = .01

print 'Welcome to the change distribution calculator!'
time.sleep(1)
while True:
	numQuarters = 0
	numDimes = 0
	numNickels = 0
	numPennies = 0
        selection = raw_input('1 to calculate, any other key to quit! ')
        if selection == '1':

		# Gets input for item price	

		itemStr = raw_input('Enter item price in the format X.XX: ')

		# Checks to see if the input was valid.  If not, exception will occur.

		try:			
                	itemPrice = float(itemStr)
			if itemPrice <= 0:
				print 'Invalid number; 0 or negative!'
				continue
		except (TypeError, ValueError):
			print 'Not a number!'
			continue

		# Gets input for cash given by customer		

		cashStr = raw_input('Enter cash given by customer in the format X.XX: ')

		# Checks to see if the input was valid.  If not, exception will occur.

		try:
			cashGiven = float(cashStr)
			if cashGiven <= 0:
				print 'Invalid number; 0 or negative!'
				continue
		except (TypeError, ValueError):
			print 'Not a number!'
			continue

		# Checks if too little money given.  If not, loop continues.

		if itemPrice > cashGiven:
			print 'Need more money from customer!'
			continue
		else:
			leftOver = round((cashGiven - itemPrice), 2)
			print 'Change: ', leftOver
			if (leftOver / quarter) >= 1:
				numQuarters = leftOver / quarter
				leftOver = round((leftOver % quarter), 2)
			if (leftOver / dime) >= 1:
				numDimes = leftOver / dime
				leftOver = round((leftOver % dime), 2)
			if (leftOver / nickel) >= 1:
				numNickels = leftOver / nickel
				leftOver = round((leftOver % nickel), 2)
			if (leftOver / penny) >= 1:
				numPennies = leftOver / penny
			
			if numQuarters >= 1:
				print 'Quarters: ', int(numQuarters)
			if numDimes >= 1:
				print 'Dimes: ', int(numDimes)
			if numNickels >= 1:
				print 'Nickels: ', int(numNickels)
			if numPennies >= 1:
				print 'Pennies: ', int(numPennies)
			
			continue

	else:
		print 'Goodbye!'
	break
