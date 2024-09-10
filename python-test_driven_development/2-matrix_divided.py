#!/usr/bin/python3
"""
divide a matrix
"""
def matrix_divided(matrix, div):
    """
    Arg:
        matrix: list of ints and floats
        div: divide

    Returns:
        list of floats divided to .2

    Raises:
        TypeError: if not ints or floats
        TypeError: not same size
        TypeError: if divisible is not number
        ZeroDivisionError: divisible by 0

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div , 2) for element in row] for row in matrix]

    return new_matrix

matrix = [
        [1, 2, 3],
        [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

