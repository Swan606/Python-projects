import random

option = ["Rock", "Paper", "Scissors"]

choice = random.choice(option)

Uchoice = input("Please choose Rock, Paper or Scissors.")

while Uchoice.upper() == "ROCK" or "PAPER" or "SCISSORS":
	if choice.upper() == Uchoice.upper():
		print("It's a draw:)")
		break
	elif choice.upper() == "ROCK" and Uchoice.upper() == "PAPER":
		print("You have won. I choose Rock.")
		break
	elif choice.upper() == "SCISSORS" and Uchoice.upper() == "PAPER":
		print("I won. I choose Scissors.")
		break
	elif choice.upper() == "ROCK" and Uchoice.upper() == "SCISSORS":
		print("I won. I choose Rock.")
		break
	elif choice.upper() == "SCISSORS" and Uchoice.upper() == "ROCK":
		print("You have won. I choose Scissors.")
		break
	elif choice.upper() == "PAPER" and Uchoice.upper() == "ROCK":
		print("I won. I choose Paper.")
		break
	elif choice.upper() == "PAPER" and Uchoice.upper() == "SCISSORS":
		print("You have won. I choose Paper.")
		break
	else:
		Uchoice = input("Wrong input.Please choose Rock, Paper or Scissors.")
	
else:
	Uchoice = input("Wrong input.Please choose Rock, Paper or Scissors.")

	
	
	

	

