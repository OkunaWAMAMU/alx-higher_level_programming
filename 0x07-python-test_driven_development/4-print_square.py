#!/usr/bin/python3

def print_square(size):
    """
    Prints a square made of '#' characters with the given size.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or is a float less than 0.
        ValueError: If size is less than 0.

    Returns:
        None
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square with '#' characters
    for _ in range(size):
        print("#" * size)
