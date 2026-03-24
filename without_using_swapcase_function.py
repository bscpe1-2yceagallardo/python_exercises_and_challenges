# Input for a text
text = input("Enter a string: ")

# Same function without swapcase() function
result = ""
for characters in text:
    # Convert uppercase to lowercase
    if 'A' <= characters <= 'Z':
        result += chr(ord(characters) + 32)
    # Convert lowercase to uppercase
    elif 'a' <= characters <= 'z':
        result += chr(ord(characters) - 32)
    else:
        result += characters  # Non-alphabet characters remain unchanged