import random

def play():
    options = ['rock', 'paper', 'scissors']
    user = input("Enter your choice (rock, paper, or scissors): ").lower().strip()

    if user not in options:
        print("Invalid input. Please choose rock, paper, or scissors.")
        return

    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie.")
    elif is_user_winner(user, computer):
        print("You win!")
    else:
        print("You lose.")

def is_user_winner(player, opponent):
    return (
        (player == "rock" and opponent == "scissors") or
        (player == "scissors" and opponent == "paper") or
        (player == "paper" and opponent == "rock")
    )

play()
