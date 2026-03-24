# Input for a text and prefix to check
text = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")

# Printing and checking if the first part of the string matches the prefix
if len(prefix) > len(text):
    print(False)
else:
    print(text[:len(prefix)] == prefix)