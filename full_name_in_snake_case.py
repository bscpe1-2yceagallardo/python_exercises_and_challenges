# Ask for a name
name = input("Enter your full name: ")

# Print name in snake case
snake = "_".join(name.lower().split())
print(snake)