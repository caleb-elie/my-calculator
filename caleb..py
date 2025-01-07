import random

options = ("rock", "paper", "scissors")
isRunning = True

while isRunning:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    if input("Play again? (y/n): ").lower() != 'y':
        isRunning = False

print("Thanks for playing!")