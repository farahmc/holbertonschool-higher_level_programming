#!/usr/bin/python3
"""A class Square with private instance attribute size
    Instantiation with size
    raise errors if size is not an int or less than 0
    raise errors if position is not a tuple or elements not integers
    Public instance method area which returns the square area
    Public instance method my_print to print square"""


class Square:
    """A class Square

    Instantiation with size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    """Get the position of the square"""
    @property
    def position(self):
        return self.__position

    """Set the position of the square"""
    @position.setter
    def position(self, value):
        if (
                isinstance(self.__position, tuple) is False
                or all(isinstance(element, int) for element in value) is False
                or all(isinstance(element >= 0 for element in value)) is False
                or len(value) != 2
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """Returns the square area"""
    def area(self):
        return (self.__size**2)

    """Prints a square"""
    def my_print(self):
        if self.__size == 0:
            print()

        for row in range(self.__position[1]):
            print()

        for row in range(self.__size):
            for col in range(self.__position[0]):
                print(" ", end="")
            for col in range(self.__size):
                print("#", end="")
            print()
