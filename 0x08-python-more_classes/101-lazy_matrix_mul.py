#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's dot function.

    Args:
        m_a (list of list of ints/floats): The first matrix.
        m_b (list of list of ints/floats): The second matrix.

    Returns:
        numpy.ndarray: The result of the multiplication.
    """
    return np.dot(m_a, m_b)
