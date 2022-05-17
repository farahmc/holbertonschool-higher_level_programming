#!/usr/bin/python3
"""
    A class Square with private instance attribute size
    Instantiation with size
    raise errors if size is not an int or less than 0
    raise errors if position is not a tuple or elements not integers
    Public instance method area which returns the square area
    Public instance method my_print to print square
"""


class Square:
    """
    A class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiation with size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (
                not isinstance(position, tuple)
                or len(position) != 2
                or not all(isinstance(element, int) for element in position)
                or position[0] < 0
                or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """
        Get the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square
        """
        if (
                not isinstance(self.__position, tuple)
                or len(value) != 2
                or not all(isinstance(element, int) for element in value)
                or position[0] < 0
                or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the square area
        """
        return (self.__size**2)

    def my_print(self):
        """
        Prints a square
        """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for col in range(self.__position[0]):
                    print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """
        a Square instance should have the same behaviour as my_print
        """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for col in range(self.__position[0]):
                    print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                if row != self.__size - 1:
                    print()
        return ("")
