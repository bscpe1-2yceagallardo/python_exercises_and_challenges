# Input for a text and substring to find
text = input("Enter a string: ")
substr = input("Enter the substring to find: ")

# Same function but without rindex() function
found = False
for i in range(len(text) - len(substr), -1, -1):  # Loop backwards
    if text[i:i+len(substr)] == substr:
        print("Last occurrence index:", i)
        found = True
        break

# Print if substring not found
if not found:
    print("Substring not found")