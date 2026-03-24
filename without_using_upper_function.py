# Input for a text
text = input("Enter a string: ")
result = ""

# Loop for converting lowercase letters to uppercase
for i in text:
    if 'a' <= i <= 'z':
        result +=chr(ord(i)-32)
    else:
        result += i