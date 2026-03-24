# Input for a text and total width
text = input("Enter a number string: ")
width = int(input("Enter the total width: "))

# Same function but without zfill() function
spaces = width - len(text)
if spaces > 0:
    text = "0" * spaces + text

# Print after zfill()
print("After zfill():", text)