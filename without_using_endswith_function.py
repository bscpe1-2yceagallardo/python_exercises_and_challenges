# Input for a text and suffix to check
text = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")

# Printing and checking if the last part of the string matches the suffix
if len(suffix) > len(text):
    print(False)
else:
    print(text[-len(suffix):] == suffix)