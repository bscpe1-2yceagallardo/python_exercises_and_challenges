odd_numbers = 0
# How many Odd numbers
for i in range(10):
    # Ask ten numbers
    input_numbers = int(input("Please input ten numbers:  "))
    # If odd numbers
    if input_numbers % 2 != 0:
        odd_numbers += 1
print(f"The count of Odd numbers is {odd_numbers}.")