#!/usr/bin/python3
"""
A class to display a representation of a rectangle
"""


class Rectangle:
    """
    Defines a representation of a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a rectangle

        Arguments:
        width - width of rectangle
        height - height of rectangle
        x - x
        y - y
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    