numbers = []
unique_numbers = []

# Loop for displaying first entry of duplicate numbers
for i in range(10):
    # Ask 10 numbers
    num = int(input(f"Please input number {i+1}: "))
    numbers.append(num)
    if num not in unique_numbers:
        unique_numbers.append(num)
