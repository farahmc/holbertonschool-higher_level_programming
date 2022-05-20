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
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0 or div == -0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    length = len(matrix[0])
    print(length)
    for row in matrix:
        print(f"length of row elements: {len(row)}")
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")

    new_list = [list(map(lambda element: round(element/div, 2), row)) for row in  matrix] 
    return new_list
