# Ask for a name
name = input("Enter your full name: ")

# Find the last non-space character
i = len(name) - 1
while i >= 0 and name[i] == " ":
    i -= 1

# Slice up to the last non-space character
print("After rstrip():", name[:i+1])