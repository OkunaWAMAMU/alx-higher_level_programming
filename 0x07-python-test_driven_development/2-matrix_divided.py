#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): The input matrix containing integers or floats.
        div (int or float): The divisor for division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if div is not an integer or float,
                   or if any row of the matrix has a different size.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists: A new matrix with all elements divided by div,
                       rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists of integers/floats
    if not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows of the matrix have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float) and not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
