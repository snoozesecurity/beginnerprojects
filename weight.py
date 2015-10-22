penny = 2.5
nickel = 5
dime = 2.268
quarter = 5.67
gramPerPound = 453.592
pennyPerWrapper = 50
nickelPerWrapper = 40
dimePerWrapper = 50
quarterPerWrapper = 40
illegalWeight = 'Illegal weight!  Goodbye!'
illegalChoice = 'Illegal choice! Goodbye!'
type1 = 'pennies!'
type2 = 'nickels!'
type3 = 'dimes!'
type4 = 'quarters!'
message1 = 'You will need'
message2 = 'wrappers for your'

poundsOrGrams = input('Are you entering your weight in pounds or grams? 1 for pounds, 2 for grams: ')
if poundsOrGrams == 1:

	# Calculations for pennies	

	pounds = input('Enter penny weight in pounds: ')
	if pounds > 0:
		weightInGrams = gramPerPound * float(pounds)
	else:
		print illegalWeight
		quit()
	numPennies = weightInGrams / float(penny)
	numPennyWrappers = int(numPennies) / pennyPerWrapper
	
	# Calculations for nickels

	pounds = input('Enter nickel weight in pounds: ')
	if pounds > 0:
		weightInGrams = gramPerPound * float(pounds)
	else:
		print illegalWeight
		quit()
	numNickels = weightInGrams / float(nickel)
	numNickelWrappers = int(numNickels) / nickelPerWrapper

	# Calculations for dimes

	pounds = input('Enter dime weight in pounds: ')
	if pounds > 0:
		weightInGrams = gramPerPound * float(pounds)
	else:
		print illegalWeight
		quit()
	numDimes = weightInGrams / float(dime)
	numDimeWrappers = int(numDimes) / dimePerWrapper

	# Calculations for quarters

	pounds = input('Enter quarter weight in pounds: ')
	if pounds > 0:
		weightInGrams = gramPerPound * float(pounds)
	else:
		print illegalWeight
		quit()
	numQuarters = weightInGrams / float(quarter)
	numQuarterWrappers = int(numQuarters) / quarterPerWrapper

elif poundsOrGrams == 2:
	
	# Calculations for pennies

	grams = input('Enter penny weight in grams: ')
	if grams <= 0:
		print illegalWeight
		quit()
	else:
		numPennies = grams / float(penny)
		numPennyWrappers = int(numPennies) / pennyPerWrapper
	
	# Calculations for nickels
	
	grams = input('Enter nickel weight in grams: ')
        if grams <= 0:
		print illegalWeight
		quit()
        else:
		numNickels = grams / float(nickel)
		numNickelWrappers = int(numNickels) / nickelPerWrapper
	
	# Calculations for dimes

	grams = input('Enter dime weight in grams: ')
	if grams <= 0:
		print illegalWeight
		quit()
	else:
		numDimes = grams / float(dime)
		numDimeWrappers = int(numDimes) / dimePerWrapper

	# Calculations for quarters

	grams = input('Enter quarter weight in grams: ')
	if grams <= 0:
		print illegalWeight
		quit()
	else:
		numQuarters = grams / float(quarter)
		numQuarterWrappers = int(numQuarters) / quarterPerWrapper
else:
	print illegalChoice
	quit()

print message1, numPennyWrappers, message2, type1
print message1, numNickelWrappers, message2, type2
print message1, numDimeWrappers, message2, type3
print message1, numQuarterWrappers, message2, type4

