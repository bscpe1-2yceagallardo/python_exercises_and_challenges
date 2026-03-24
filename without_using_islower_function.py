# Input for a text
text = input("Enter a string: ")

is_lower = True
# Checking if any letter is uppercase, it's not all lowercase
for i in text:
    if 'A' <= i <= 'Z':
        is_lower = False
        break

# Printing true if string is all in lowercase
print("All letters are lowercase:", is_lower)