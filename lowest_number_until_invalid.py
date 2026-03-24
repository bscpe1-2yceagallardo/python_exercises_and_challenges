nums = []
# Logic of until valid
while True:
    # Ask numbers
    input_numbers = (input("Enter a number: "))
    if not input_numbers.isdigit(): break
    nums.append(int(input_numbers))

# Printing and condition for lowest number
if nums:
    print("Lowest number:", min(nums))
else:
    print("No valid numbers entered.")
