#!/usr/bin/python3
"""
A class that raises an exception
"""


class BaseGeometry:
    """
    A class that raises an exception
    """
    def area(self):
        """
        Raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check if value is an integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
