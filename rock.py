from random import randint
print("Rock...")
print("Paper...")
print("Scissors...")
x = input("Enter the number of rounds you want to play:")
for a in range(0, x):
    player = input("Player, make your move: ").lower()
    rand_num = randint(0, 2)
    if rand_num == 0:
    	computer = "rock"
    elif rand_num == 1:
    	computer = "paper"
    elif rand_num ==2 :
	computer = "scissors"

    print(f"Computer plays {computer}")

    if player == computer:
    	print("It's a tie!")
    elif player == "rock":
    	if computer == "scissors":
        	print("player wins!")
    	else:
    	    print("computer wins!")
    elif player == "paper":
    	if computer == "rock":
        	print("player wins!")
    	else:
        	print("computer wins!")
	
	elif player =="scissors":
   		if computer == "paper":
   	    	print("player wins!")
    	else:
        	print("computer wins!")
    else:
    	print("Please enter a valid move!")
