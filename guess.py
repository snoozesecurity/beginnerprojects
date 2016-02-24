# Problem taken from r/beginnerprojects
# Code written by SnoozeSecurity (youtube.com/channel/UCa5QaVWjwFkUNoLtMka1d3w)

import random
import time

isPlaying = True

# Establishes loop so player can play multiple times if he/she would like

while isPlaying == True:
	guesses = 0 # Keeps track of guesses throughout game loop
	gameNum = random.randint(1, 100) # Generates random number between 1 and 100
	print "Welcome to the guessing game!\n"
	time.sleep(1)
	print "To play, simply guess a number between 1 and 100.\n"
	time.sleep(.5)
	print "The lower the number of guesses you make, the smarter you are, or something.\n"
	time.sleep(1)
	while True: # Secondary loop for user input; only accepts integers between 1 and 100. Keeps track of guesses
		userGuess = raw_input("Enter a guess between 1 and 100: ")
		try:
			userGuess = int(userGuess)
		except (TypeError, ValueError, NameError):
			print 'Not an integer, try again!'
			continue
		if (userGuess > gameNum and userGuess <= 100):
			print ("Too high!")
			guesses = guesses + 1
		elif (userGuess < gameNum and userGuess >= 1):
			print ("Too low!")
			guesses = guesses + 1
		elif userGuess == gameNum:
			print ("You are correct!")
			guesses = guesses + 1
			print "You took", guesses, "guesses to correctly find the number."
			break
		else:
			print ("Out of bounds; choose between 1 and 100!")
			
	time.sleep(1)
	
	# Checks to see if player wants to play again, quits if not
	
	playAgain = raw_input("Play again? Y for yes, any other key for no. ") 
	if (playAgain != "Y" and playAgain != "y"):
		isPlaying = False
		print "Goodbye!"
	

			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		