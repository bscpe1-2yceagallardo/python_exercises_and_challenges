# Input for a text and total width
text = input("Enter a string: ")
width = int(input("Enter the total width: "))

# Condition of adding spaces at the end to reach desired width
spaces = width - len(text)
if spaces > 0:
    text = text + " " * spaces

# Print the text with desired ends-width spaces
print("After ljust():", text)