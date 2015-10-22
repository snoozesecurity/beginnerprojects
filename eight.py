# Problem taken from r/beginnerprojects
# Inefficient code by SnoozeSecurity (youtube.com/channel/UCa5QaVWjwFkUNoLtMka1d3w)
# I am not a professional programmer, rather someone trying to learn python :)

import random
import time

thinking = ['Just a moment...', 'Be right with you.', 'Hold your horses!', 'Thinking...', 'Be back soon.']
responses = ['Hmmm, the truth escapes me.', 'The world may never know.', 'Survey says...probably, maybe.', 'Nope', 'Absolutely']

print 'Welcome to the Magic 8 ball!'
while True:
	question = raw_input('What question do you have for me today? Q to quit!\n' )
	if question != 'Q':
		print random.choice(thinking)
		time.sleep(1)
		print random.choice(responses)
		time.sleep(.5)
	else:
		print 'Goodbye!'
		break

