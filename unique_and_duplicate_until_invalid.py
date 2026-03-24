nums = set()
# Loop for until valid
while True:
    # Ask for numbers
    input_numbers = input("Enter a number: ")
    if not input_numbers.isdigit(): break

    # Condition for "Unique" and "Duplicate"
    if_num = int(input_numbers)
    print("Duplicate" if if_num in nums else "Unique")
    nums.add(if_num)
