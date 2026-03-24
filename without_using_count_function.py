# Input for a text and character to count
text = input("Enter a string: ")
char = input("Enter the character to count: ")

# Same function but without count() function
count = 0
for character in text:
    if character == char:
        count += 1