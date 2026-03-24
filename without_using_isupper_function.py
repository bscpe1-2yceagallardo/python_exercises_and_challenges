# Input for a text
text = input("Enter a string: ")

is_upper = True
# Checking if any letter is lowercase, it's not all uppercase
for characters in text:
    if 'a' <= characters <= 'z':
        is_upper = False
        break