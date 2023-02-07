import random

def play_again():
  question = 'Do You want to play again? y = yes, n = no \n'
  play_game = input(question)
  while play_game.lower() not in ['y', 'n']:
      play_game = input(question)

  if play_game.lower() == 'y':
      return True
  else:
      return False

def Hangman(word):
	display = "_"* len(word)
	count = 0
	limit = 5
	letters = list(word)
	guessed = []
	while count < limit:
		guess = input("Please guess a letter.")
		while len(guess) != 1:
			print("Invalid input. Please guess one letter.")
			guess = input("Please guess a letter.")
			 
		if guess in letters:
			letters.remove(guess)
			index = word.find(guess)
			display = display[:index] + guess + display[index + 1:]
			print(display)

		else:
			guessed.append(guess)
			count += 1
			if count == 1:
			    print('   _____ \n'
				  '  |      \n'
				  '  |      \n'
				  '  |      \n'
				  '  |      \n'
				  '  |      \n'
				  '  |      \n'
				  '__|__\n')
			    print('Wrong guess:' + str(limit - count) + ' guesses remaining\n')

			elif count == 2:
			    print('   _____ \n'
				  '  |     | \n'
				  '  |     | \n'
				  '  |      \n'
				  '  |      \n'
				  '  |      \n'
				  '  |      \n'
				  '__|__\n')
			    print('Wrong guess:' + str(limit - count) + ' guesses remaining\n')

			elif count == 3:
			    print('   _____ \n'
				  '  |     | \n'
				  '  |     | \n'
				  '  |     | \n'
				  '  |      \n'
				  '  |      \n'
				  '  |      \n'
				  '__|__\n')
			    print('Wrong guess:' + str(limit - count) + ' guesses remaining\n')

			elif count == 4:
			    print('   _____ \n'
				  '  |     | \n'
				  '  |     | \n'
				  '  |     | \n'
				  '  |     O \n'
				  '  |      \n'
				  '  |      \n'
				  '__|__\n')
			    print('Wrong guess:' + str(limit - count) + ' guesses remaining\n')

			elif count == 5:
			    print('   _____ \n'
				  '  |     | \n'
				  '  |     | \n'
				  '  |     | \n'
				  '  |     O \n'
				  '  |    /|\ \n'
				  '  |    / \ \n'
				  '__|__\n')
			    print('Wrong guess. You\'ve been hanged!!!\n')
			    print('The word was: ' + str(word))
			    
		if display == word:
			print('Congrats! You have guessed the word ' + str(word) + ' correctly!')
			break
			


def play_Hangman():

	words_to_guess = [ 'image', 'film', 'promise', 'kids', 'lungs', 'rhyme', 'plants', 'world' ]
	play = True
	while play:
       		word = random.choice(words_to_guess)
       		Hangman(word)
       		play = play_again()
	print('Thanks For Playing!')
	exit()	

play_Hangman()










