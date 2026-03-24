# Input for a text
text = input("Enter a string: ")
result = ""

# Loop for converting uppercase letters to lowercase
for characters in text:
    if 'A' <= characters <= 'Z':
        result += chr(ord(characters) + 32)
    else:
        result += characters