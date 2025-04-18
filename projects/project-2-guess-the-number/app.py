import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100...")
    print("You have only 3 attempts to guess!")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 3
    guess = None

    while guess != secret_number and attempts < max_attempts:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low.")
            elif guess > secret_number:
                print("Too high.")
            else:
                print(f"Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} tries.")
                break

        except ValueError:
            print("Please enter a valid number.")

    if guess != secret_number:
        print("Sorry! You've used all your attempts.")
        print(f"The correct number was {secret_number}.")


guess_the_number()
