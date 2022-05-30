#!/usr/bin/python3
"""
A module that creates a class names BaseGeometry
"""


class BaseGeometry:
    """
    A class that raises an exception and checks if a value
    is an integer >0

    Attributes:
    area - raises an exception
    integer_validator - checks if value is an integer >0
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
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
