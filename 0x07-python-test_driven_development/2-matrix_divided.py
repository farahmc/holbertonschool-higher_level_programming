#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Arguments:
    Matrix - list of equal length lists of integers or floats
    Div - number to divide elements by (must be non-zero integer or float)

    Returns:
    New matrix with quotients to 2 decimal places
    """
    """if (
        not all(isinstance(element, int) for element in matrix)
        and not all(isinstance(element, float) for element in matrix)
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")"""

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0 or div == -0:
        raise ZeroDivisionError("division by zero")

    """if not all(len(row) == len(matrix[0]) for row in matrix:
        raise TypeError("Each row of the matrix must have the same size")"""

    return [list(map(lambda element: round(element/div, 2), row)) for row in  matrix]
