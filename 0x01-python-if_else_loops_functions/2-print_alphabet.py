#!/usr/bin/python3

for char_code in range(ord('a'), ord('z') + 1):
    print("{:c}".format(char_code), end='')

# Print a newline at the end
print()
