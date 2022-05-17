#!/usr/bin/python3
class Square:
    """A class Square with private instance attribute size
    Instantiation with size
    raise errors if size is not an int or less than 0"""

    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
