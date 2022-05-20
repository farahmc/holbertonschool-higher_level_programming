#!/usr/bin/python3
"""
Function to add 2 integers or floats
"""


def add_integer(a, b=98):
    """
    Sums the 2 given variables, which must be an integer or float
    Returns the sum as an integer
    """
    if isinstance(a, int) is False and isinstance(a, float) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False and isinstance(b, float) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
