even_counter = 0
for i in range(10):
    # Ask ten numbers
    input_numbers = int(input("Please input numbers:  "))
    # How many even numbers
    if input_numbers % 2 == 0:
        even_counter += 1
print(even_counter)
