import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input ("Type Rock/Paper/Scissors or Q to Quit:").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        print("You haven't typed Eihter Rock/Paper/Scissors or Q")
        continue

    random_number = random.randint(0,2)
    # Rock : 0, Paper : 1, Scissors : 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
        

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
        

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
        
    else:
        print("You lost!")
        computer_wins += 1

print("You Won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye !!!")