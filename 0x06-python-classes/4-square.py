#!/usr/bin/python3
class Square:
    """A class Square with private instance attribute size
    Instantiation with size
    raise errors if size is not an int or less than 0
    Public instance method area which returns the square area"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size**2)
