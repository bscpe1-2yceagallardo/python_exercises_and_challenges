nums = []
# Loop for until valid
while True:
    # Ask for numbers
    input_numbers = input("Enter a number: ")
    if not input_numbers.isdigit(): break
    nums.append(int(input_numbers))

# Printing and sorting lowest to highest
nums.sort()
print("Numbers from lowest to highest:", nums)

