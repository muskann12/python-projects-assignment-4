def computer_guesses():
    print("Think of a number between 1 and 100, and I will try to guess it!")
    print("When I guess, reply with:")
    print("'h' if my guess is too high")
    print("'l' if my guess is too low")
    print("'c' if my guess is correct")

    low = 1
    high = 100
    feedback = ''

    while feedback != 'c' and low <= high:
        guess = (low + high) // 2  # computer uses binary search
        print(f"My guess is: {guess}")
        feedback = input("Is it too High (h), too Low (l), or Correct (c)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"I guessed it! Your number was {guess}.")
            break
        else:
            print("Please enter only 'h', 'l', or 'c'.")

    if low > high:
        print("Hmm, something went wrong. Did you cheat? 😅")

# Start the game
computer_guesses()
