# Input for a text
text = input("Enter a string: ")

# Same function without capitalize() function
if len(text) > 0:
    result = ""

    for i in range(len(text)):
        characters = text[i]
        # First character → uppercase
        if i == 0 and 'a' <= characters <= 'z':
            result += chr(ord(characters) - 32)
        # Remaining characters → lowercase
        elif i != 0 and 'A' <= characters <= 'Z':
            result += chr(ord(characters) + 32)
        else:
            result += characters
    # Print into capitalized
    print("Capitalized string:", result)
else:
    print(text)
