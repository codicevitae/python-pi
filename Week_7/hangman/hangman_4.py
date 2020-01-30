# Version 4
#
# Let's not use the same word everytime
#

import random

#
# This function picks a word at random from a list
#
def pick_word():
	words = [ 'apple', 'pickle', 'orange', 'bannana', 'refulgence', 'superstitious',
		  'refrigerator', 'omelette', 'latte', 'ocean', 'indulgence', 'propitiation' ]

	return words[random.randrange(len(words))]

#
# This function prints the word with blanks for letters that have
# not been guessed
#
def show_blanked_out(word, guesses):
	blanked = ''
	for letter in word:
		if letter in guesses:
			blanked = blanked + letter + ' '
		else:
			blanked = blanked + '_ '	

	print(blanked)
	print('\n')


# Our main program
def game():
	print('Welcome to Hangman!\n')

	MAX_GUESSES = 5
	incorrect_guesses = 0

	# When you pass the list function a string it creates a list containing each letter
	secret_word = list(pick_word())

	correct_guesses = []
	incorrect_guesses = []

	while len(incorrect_guesses) < MAX_GUESSES:
		guess = input('Enter a letter: ')

		# The 'in' operator can check if a string is in a list (or another string)
		if guess in incorrect_guesses or guess in correct_guesses:
			print('You already guessed that! Try again\n')

		elif guess in secret_word:
			print('Correct!\n')

			# One way to fix the duplicate letter problem:
			# If the guess appears more than once in the word, we need to add it
			# to our correct_guesses for each occurance. Is there a better way?
			occurances = secret_word.count(guess)
			for i in range(occurances):
				correct_guesses.append(guess)

			show_blanked_out(secret_word, correct_guesses)

			if len(correct_guesses) == len(secret_word):
				print('You win!')

				break
		else:
			incorrect_guesses.append(guess)	
			print('Incorrect!\n')
			guesses_left = MAX_GUESSES - len(incorrect_guesses)
			print(f'You have {guesses_left} guesses left!\n')


	if len(incorrect_guesses) == MAX_GUESSES:
		print('You lose!');

game()
