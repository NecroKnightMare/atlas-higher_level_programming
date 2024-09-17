#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    ret a list of ints rep pas tri of n
    """
    if n <= 0:
        n = []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j - i] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle
