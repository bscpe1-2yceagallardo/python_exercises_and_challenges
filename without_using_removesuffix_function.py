# Input for a text and suffix to remove
text = input("Enter the full text: ")
suffix = input("Enter the suffix to remove: ")

# Get the length of the suffix
n = len(suffix)

# Printing and checking if the end of 'text' matches 'suffix'
if text[-n:] == suffix:
    print("After removesuffix():", text[:-n])
else:
    print("After removesuffix():", text)