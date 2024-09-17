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

    for i in range(2, n + 1):
        prev = triangle[-1]
        row = [1]
        for j in range(1, i - 1):
            row.append(prev[j - 1] + prev[j])

        row.append(1)
        triangle.append(row)

    return triangle
