# Ask 10 numbers
numbers = [int(input("Please input ten numbers: ")) for i in range(10)]

# Loop determining numbers with no duplicate
for i in numbers:
    if numbers.count(i) == 1:
        print(i)