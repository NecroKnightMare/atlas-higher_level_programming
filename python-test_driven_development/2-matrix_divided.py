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
    if not isinstance(div, (int, float) or div == 0):
        raise ZeroDivisionError("division by zero")

    result = []

    for row in matrix:
        if not isinstance(row, list) or not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(map(len, row))) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    result_row = [round(x / div , 2) for x in row]

    result.append(result_row)

    return result
