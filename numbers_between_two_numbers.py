# Asking two numbers
first = int(input("Please input first number:  "))
last = int(input("Please input last number:  "))

# Numbers between
numbers_between = list(range(first + 1, last))

# Printing numbers between two numbers
print(f"The number/s between {first} and {last} is/are {numbers_between}.")