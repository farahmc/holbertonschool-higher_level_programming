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
        self.height = height
        self.width = width

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
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height*2) + (self.width*2)
