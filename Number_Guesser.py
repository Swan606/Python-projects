import random


User_Guess = 0
random_number = random.randrange(1,100)

while User_Guess != random_number:
	User_Guess = int(input("Please guess a number between 1 and 100: "))
	if User_Guess > random_number:
		print ("Please guess a lower number.")
	elif User_Guess == random_number:
		print("Well done.")
	else:
		print ("Please guess a higher number.")


