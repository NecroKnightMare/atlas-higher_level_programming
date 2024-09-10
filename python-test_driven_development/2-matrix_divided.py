#!/usr/bin/python3

"""
divides matrix by a given divisor
"""

def matrix_divided(matrix, div):
    """
    Args:
        matrix: list of ints and floats
        div: divide

    Raises:
        TypeError: if not ints or floats
        TypeError: not same size
        TypeError: if divisible is not number
        ZeroDivisionError: divisible by 0

    Returns:
        list of floats divided to .2

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all (len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
