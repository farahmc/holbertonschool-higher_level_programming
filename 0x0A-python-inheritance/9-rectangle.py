#!/usr/bin/python3
"""
A module with a base class BaseGeometry and inherited class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle and inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiate with width and height

        Arguments:
        width - width of rectangle
        height - height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Return the area of a rectangle
        """
        return (self.__width * self.__height)

    def __repr__(self):
        """
        Return a string representation
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
