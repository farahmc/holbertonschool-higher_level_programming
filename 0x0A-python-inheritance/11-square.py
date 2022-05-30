#!/usr/bin/python3
"""
A module with a base class BaseGeometry and inherited class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square and inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiate with size

        Arguments:
        size - width and height of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
