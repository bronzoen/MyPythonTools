import random

choice = {1:"ROCK",2:"PAPER",3:"SCISSORS"}
inputchoice = {'r':1,'p':2,'s':3}

while True:
	
	print("="*30)
	userchoice = input("ROCK(r)/PAPER(p)/SCISSORS(s) : ").lower()
	aichoice = random.randint(1,3)

	if userchoice not in inputchoice:
		print("Enter (r/p/s)!")
		continue

	userchoice = inputchoice[userchoice]

	if userchoice == aichoice:
		print(f"USER({choice[userchoice]}) VS AI({choice[aichoice]})")
		print("DRAW")
	elif (userchoice == 1 and aichoice == 3) or (userchoice == 2 and aichoice == 1) or (userchoice == 3 and aichoice == 2):
		print(f"USER({choice[userchoice]}) VS AI({choice[aichoice]})")
		print("YOU WIN")
	else:
		print(f"USER({choice[userchoice]}) VS AI({choice[aichoice]})")
		print("YOU LOSE")
	
	if input("Enter 'y' To Play Again! :").lower() == "y":
		pass
	else:
		break
