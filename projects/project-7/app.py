import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    num_passwords = int(input("How many passwords do you want to generate? "))
    length = int(input("What should be the length of each password? "))

    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        print(generate_password(length))

except ValueError:
    print("Please enter valid numbers.")
