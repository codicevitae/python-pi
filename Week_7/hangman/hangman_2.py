# Version 2
#
# Let's fix the duplicate letter problem
#

print('Welcome to Hangman!')

MAX_GUESSES = 5
incorrect_guesses = 0

# When you pass the list function a string it creates a list containing each letter
secret_word = list('apple')

correct_guesses = []
incorrect_guesses = []

while len(incorrect_guesses) < MAX_GUESSES:
	guess = input('Enter a letter: ')

	# The 'in' operator can check if a string is in a list (or another string)
	if guess in incorrect_guesses or guess in correct_guesses:
		print('You already guessed that! Try again')
	elif guess in secret_word:
		print('Correct!')

		# One way to fix the duplicate letter problem
		# If the guess appears more than once in the word, we need to add it
		# to our correct_guesses for each occurance
		occurances = secret_word.count(guess)
		for i in range(occurances):
			correct_guesses.append(guess)

		if len(correct_guesses) == len(secret_word):
			print('You win!')
			break
	else:
		incorrect_guesses.append(guess)	
		print('Incorrect!')


if len(incorrect_guesses) == MAX_GUESSES:
	print('You lose!');
			

	
	
