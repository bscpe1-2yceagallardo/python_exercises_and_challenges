nums = []
# Loop for until valid
while True:
    # Ask for numbers
    input_numbers = input("Enter a number: ")
    if not input_numbers.isdigit(): break
    nums.append(int(input_numbers))

# Condition to display the average
if nums:
    print("Average:", sum(nums)/len(nums))
else:
    print("No valid numbers entered.")
