#!/usr/bin/python3
"""A class Square with private instance attribute size
    Instantiation with size
    raise errors if size is not an int or less than 0
    Public instance method area which returns the square area and prints
    square"""


class Square:
    """A class Square

    Instantiation with size"""
    def __init__(self, size=0):
        self.__size = size

    """Get the size of the square"""
    @property
    def size(self):
        return self.__size

    """Set the size of the square"""
    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Returns the square area"""
    def area(self):
        return (self.__size**2)

    """Prints a square"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
