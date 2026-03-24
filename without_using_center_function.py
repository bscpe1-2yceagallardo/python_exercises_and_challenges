# Input for a text and total width
text = input("Enter a string: ")
width = int(input("Enter the total width: "))

# Same function without center() function
spaces = width - len(text)
if spaces > 0:
    left = spaces // 2
    right = spaces - left
    text = " " * left + text + " " * right