import random

print("Hello Player. Welcome to Rock Paper and Scissors Game\n ")

print("<------------Game Rules--------------->\n")
print("1.Player should choose either Rock,Paper or Scissor\n2.The Computer will choose his choice\n3.Rock beats scissors (by crushing them); scissors beats paper (by cutting it); and paper beats rock (by covering it)\n4.If its tie then the game contiues till either the player is winner or the computer")

choice = ["rock","paper","scissors"]

while True:

    player_choice = input ("\nEnter rock,paper, or scissors: ")

    computer_choice = random.choice(choice)
    print(f"Computer Chose: {computer_choice}")

    if player_choice == computer_choice:
        print("Its a tie")
        
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
    	print("\nYou Win!")
    	break
    else:
    	print("\nComputer Wins!")
    	break


