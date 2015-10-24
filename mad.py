# SnoozeSecurity
# Mad Libs clone
# r/beginnerprojects
# Very little input validation!

# A long time ago there was a <man/woman> named <name>. He/she decided to <verb> a <vehicle> into a desert. The desert was <adjective>.
# Because of this, <name> drank some <drink> to cool off.  At the end of the day, the sky was <color>.

import time

story1 = 'A long time ago there was a'
story2 = 'named'
period = '.'
story4 = 'decided to'
story5 = 'a'
story6 = 'into the desert'
story7 = 'The desert was'
story8 = 'Because of this,'
story9 = 'drank some'
story10 = 'to cool off.  At the end of the day, the sky was'
counter = 0

print 'Welcome to my boring Mad Libs clone!'
time.sleep(.5)

# Gets story variable input from user

gender = raw_input('man or woman? ')
if gender.lower() == 'man':
	heOrShe = 'He'
elif gender.lower() == 'woman':
	heOrShe = 'She'
else:
	print 'Invalid! Goodbye!'
	quit()
name = raw_input('name? ')
verb1 = raw_input('verb? ')
noun1 = raw_input('vehicle? ')
adj1 = raw_input('adjective to describe weather? ')
noun2 = raw_input('type of drink? ')
adj2 = raw_input('color? ')

# Capitalizes first letter of the name

for i in name:
	counter += 1
counter = counter - 1
name = name.lower()
capName = name[:1].upper() + name[-counter:]	

# Prints the story

print story1, gender, story2, capName.format() + period
time.sleep(1)
print heOrShe, story4, verb1, story5, noun1, story6.format() + period
time.sleep(1.5)
print story7, adj1.format() + period
time.sleep(1)
print story8, capName, story9, noun2, story10, adj2.format() + period
time.sleep(2)
print 'THE END!'
time.sleep(1)
