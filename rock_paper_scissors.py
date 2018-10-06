
#Rock Paper Scissors Game
import random
#Scores
cpuwins = 0 
playerwins = 0

#Choices the computer can make
choices = ["rock", "scissors", "paper"] 

# Repetitive code here, any solutions?
while True:
	computer = random.choice(choices) # The generation of the computer's choice 
	userchoice = input("Please pick rock, paper, or scissors\n").lower() #Asks and stores the users choice 
	
	if userchoice == "rock":
		if computer == "paper":
			print("Computer's paper beats your rock.")
			cpuwins = cpuwins + 1
		elif computer == "scissors":
			print("Your rock has beaten the computer's scissors.")
			playerwins = playerwins + 1
		elif computer == "rock":
			print("Tie!")
		
	elif userchoice == "paper":
		if computer == "paper":
			print("Tie!")
		elif computer == "scissors":
			print("The computer's scissors beats your paper")
			cpuwins = cpuwins + 1
		elif computer == "rock":
			print("Your paper has beaten the computer's rock")
			playerwins = playerwins + 1
		
	elif userchoice == "scissors":
		if computer == userchoice:
			print("Tie!")
		elif computer == "rock":
			print("Your scissors has been beaten by the computer's rock.")
			cpuwins = cpuwins + 1
		elif computer == "paper":
			print("Your scissors has beaten the computer's paper.")
			playerwins = playerwins + 1
			
	#Prints scores		
	print("The current score is {} / {} (Computer wins / player wins))".format(cpuwins, playerwins))
	#Askes user if they want to replay the game
	replay = input("Would you like to play again? Please enter yes or no.\n").lower()
	if replay == "yes":
		continue
	elif replay == "no":
		break

