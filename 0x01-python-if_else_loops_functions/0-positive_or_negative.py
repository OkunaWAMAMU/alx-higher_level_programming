#!/usr/bin/python3

import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10, 10)

# Print the number
print(number, end=" ")

# Check whether the number is positive, negative, or zero and print the corresponding message
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
