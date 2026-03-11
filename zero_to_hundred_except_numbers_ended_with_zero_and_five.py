# Loop zero to one hundred
for i in range(101):
    # Except for numbers ended with zero or five
    if i % 10 not in (0,5):
        # Printing numbers without zero or five
        print(i)