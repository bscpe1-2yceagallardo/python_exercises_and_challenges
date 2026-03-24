# Ask 10 numbers
numbers = []
for i in range(10):
    numbers.append(int(input("Enter a number: ")))

# Print all numbers entered
print("\nAll numbers entered:")
print(numbers)

# Print numbers without duplicates (only first occurrence)
print("\nNumbers with first occurrence of duplicates:")
print(set(numbers))
