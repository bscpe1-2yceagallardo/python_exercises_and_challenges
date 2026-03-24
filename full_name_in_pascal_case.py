# Ask for a name
name = input("Enter your full name: ")

# Print name in pascal case
print("".join(word.capitalize() for word in name.split()))