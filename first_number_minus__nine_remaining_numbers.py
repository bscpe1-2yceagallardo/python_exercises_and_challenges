result = 0
# Loop of first number minus remaining numbers
for i in range(10):
    # Ask ten numbers
    numbers = int(input("Please input ten numbers. First number to be subtracted by nine numbers:  "))
    if i == 0:
        result = numbers
    else:
         result -= numbers
print(f"The answer for first number minus remaining number is {result}.")