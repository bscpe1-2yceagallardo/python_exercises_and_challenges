# Ask for a name
name = input("Enter your full name: ")

# Find the first non-space character
i = 0
while i < len(name) and name[i] == " ":
    i += 1

# Slice from the first non-space character
print("After lstrip():", name[i:])