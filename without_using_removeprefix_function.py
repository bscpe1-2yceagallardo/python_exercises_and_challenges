# Input for a text and prefix to remove
text = input("Enter the full text: ")
prefix = input("Enter the prefix to remove: ")

# Get the length of the prefix
length_prefix = len(prefix)

# Printing and checking if the start of 'text' matches 'prefix'
if text[:length_prefix] == prefix:
    print("After removeprefix():", text[length_prefix:])
else:
    print("After removeprefix():", text) 