nums = []
# Logic of until valid
while True:
    # Ask numbers
    input_numbers = int(input("Enter a number: "))
    if not input_numbers.isdigit(): break
    nums.append(input_numbers)