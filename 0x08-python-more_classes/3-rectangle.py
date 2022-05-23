#!/usr/bin/python3
"""
Representation of a rectangle
"""


class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialise a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns area of rectangle
        """
        return (self.height*self.width)

    def perimeter(self):
        """
        Returns perimeter of rectangle
        """
        return (self.height*2) + (self.width*2)

    def __str__(self):
        """
        Return a string representation of the class instance"
        """
        string_rep = ""
        if self.width == 0 or self.height == 0:
            return string_rep
        for row in range(self.height):
            for col in range(self.width):
                string_rep += "#"
            if row < (self.__height - 1):
                string_rep += "\n"
        return string_rep
