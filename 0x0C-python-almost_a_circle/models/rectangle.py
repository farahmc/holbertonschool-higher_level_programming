#!/usr/bin/python3
"""
A class to display a representation of a rectangle
"""
from models.base import Base


class Rectangle(Base):
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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width """
        self.__width = value

    @property
    def height(self):
        """ Get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height """
        self.__height = value

    @property
    def x(self):
        """ Get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set x """
        self.__x = value

    @property
    def y(self):
        """ Get y """
        return self.__y

    @y.setter
        """ Set y """
    def y(self, value):
        self.__y = value
