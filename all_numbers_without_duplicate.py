# Ask 10 numbers
numbers = [int(input("Please input ten numbers: ")) for _ in range(10)]

# Loop determining numbers with no duplicate
for i in numbers:
    if numbers.count(i) == 1: