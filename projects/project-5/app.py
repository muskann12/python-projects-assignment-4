import random

# 1. Word list — yeh wo words hain jo computer choose kar sakta hai
words = ['apple', 'banana', 'grapes', 'mango', 'orange']

# 2. Computer random word choose karega
secret_word = random.choice(words)

# 3. Game ke liye setup
guessed_letters = []  # User ne ab tak kya guess kiya
tries = 6             # Total wrong tries allowed

print("Welcome to Simple Hangman Game!")
print("_ " * len(secret_word))  # secret word jitne letters hai, utni underscores dikhengi

# 4. Game loop
while tries > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
    else:
        tries -= 1
        print("Wrong guess! Tries left:", tries)

    # 5. Word ka current status show karo
    display = ''
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    print(display)

    # 6. Check karo ke user ne poora word guess kar liya?
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 You won! The word was:", secret_word)
        break

if tries == 0:
    print("😢 You lost. The word was:", secret_word)
