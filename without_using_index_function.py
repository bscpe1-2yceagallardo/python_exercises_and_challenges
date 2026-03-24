# Input for a text and substring to find
text = input("Enter a string: ")
substr = input("Enter the substring to find: ")

# Same function but without index() function
found = False
for i in range(len(text) - len(substr) + 1):
    if text[i:i+len(substr)] == substr:
        print("First occurrence index:", i)
        found = True
        break

# Print if substring not found
if not found:
    print("Substring not found")