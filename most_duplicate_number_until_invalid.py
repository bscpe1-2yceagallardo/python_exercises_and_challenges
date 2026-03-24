nums = []
# Loop for until valid
while True:
    # Ask for numbers
    input_numbers = input("Enter a number: ")
    if not input_numbers.isdigit(): break
    nums.append(int(input_numbers))

# Condition of number with most duplicates
if nums:
    most = max(nums, key=nums.count)
    print("Number with most duplicates:", most)
else:
    print("No valid numbers entered.")
