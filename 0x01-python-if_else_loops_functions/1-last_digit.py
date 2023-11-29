#!/usr/bin/python3

import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10000, 10000)

# Calculate the last digit of the number
last_digit = abs(number) % 10 if abs(number) != 0 else 0

# Print the result
print(f"Last digit of {number} is {last_digit}", end=" ")

# Determine if the last digit is greater than 5, 0, or less than 6 and not 0
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

