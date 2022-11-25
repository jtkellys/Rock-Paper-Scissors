import random

list = ("rock", "paper", "scissors")
game = True
user_count = 0
computer_count = 0

while game:
    print("Let's play rock, paper, scissors")
    print(f"Computer Wins: {computer_count}")
    print(f"Player Wins: {user_count}")
    play = input("Would you like to play? (yes or no): ")
    if play == "yes":
        player_choice = input("Select rock, paper, or scissors: ")
        print("You chose " + player_choice)
        computer_choice = random.choice(list)
        print("Computer chooses " + computer_choice)

        if player_choice == computer_choice:
            result = "It's a Tie!!"
            print(result)
        elif player_choice == "rock" and computer_choice == "paper":
            result = "Computer Wins!"
            computer_count += 1
            print(result)
        elif player_choice == "rock" and computer_choice == "scissors":
            result = "Player Wins!"
            user_count += 1
            print(result)
        elif player_choice == "paper" and computer_choice == "rock":
            result = "Player Wins!"
            user_count += 1
            print(result)
        elif player_choice == "paper" and computer_choice == "scissors":
            result = "Computer Wins!"
            computer_count += 1
            print(result)
        elif player_choice == "scissors" and computer_choice == "rock":
            result = "Computer Wins!!"
            computer_count += 1
            print(result)
        elif player_choice == "scissors" and computer_choice == "paper":
            result = "Player Wins!"
            user_count += 1
            print(result)
        else:
            break
    elif play == "no":
        print("Have a good day!")
        break
