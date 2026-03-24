# Input for a text
text = input("Enter a string: ")

# Same function without title() function
result = ""
new_word = True  # Flag to detect start of a word

for characters in text:
    if characters == " ":
        result += characters
        new_word = True  # Next character starts a new word
    else:
        if new_word and 'a' <= characters <= 'z':
            result += chr(ord(characters) - 32)  # Capitalize first letter
        elif not new_word and 'A' <= characters <= 'Z':
            result += chr(ord(characters) + 32)  # Lowercase other letters
        else:
            result += characters
        new_word = False