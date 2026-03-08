# Ask 2 numbers
num1 = float(input("Please input first number:  "))
num2 = float(input("Please input second number: "))

# Bigger number
if num1 > num2:
    print(f"The bigger number is: {num1}")
elif num2 > num1:
    print(f"The bigger number is: {num2}")
else:
    print(f"The numbers are equal.")
