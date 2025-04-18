# Mad Libs Game

print("Mad Libs Game - Let's make a funny story!\n")

# Inputs from user
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
verb = input("Enter a verb (like running, jumping): ")
emotion = input("Enter an emotion (happy, sad, etc): ")

# Making a funny story
story = f"One day, {name} went to {place}. There, they saw a {animal} eating {food}!\n\
{name} started {verb} and felt very {emotion}. What a weird day!"

# Show the story
print("\nHere's your Mad Libs story:")
print(story)
