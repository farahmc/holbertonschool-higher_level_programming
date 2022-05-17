#!/usr/bin/python3
"""A class Square with private instance attribute size
    Instantiation with size
    raise errors if size is not an int or less than 0
    Public instance method area which returns the square area"""


class Square:
    """A class Square"""
    def __init__(self, size=0):
        """Raise errors if size is not an int or less than 0"""
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """Instantiate with size"""
        self.__size = size

    """Returns the square area"""
    def area(self):
        return (self.__size**2)
