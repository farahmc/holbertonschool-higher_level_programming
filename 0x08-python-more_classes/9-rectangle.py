#!/usr/bin/python3
"""
Representation of a rectangle
"""


class Rectangle:
    """
    Representation of a rectangle

    Attributes:
    number_of_instances: Number of instances of class Rectangle
    print_symbol: character to print to represent a rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialise a rectangle.

        Arguments:
        width: width of rectangle
        height: height of rectangle
        """
        type(self).number_of_instances += 1
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
        return (self.height*2) + (self.width*2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance where height and width are equal
        to size
        """
        return cls(size, size)

    def __str__(self):
        """
        Return a printable representation
        """
        string_rep = ""
        if self.width == 0 or self.height == 0:
            return string_rep
        for row in range(self.height):
            for col in range(self.width):
                string_rep += str(self.print_symbol)
            if row < (self.__height - 1):
                string_rep += "\n"
        return string_rep

    def __repr__(self):
        """
        Return a string representation
        """
        return f'Rectangle({self.width},{self.height})'

    def __del__(self):
        """
        Print a message every time Rectangle is deleted
        """
        print('Bye rectangle...')
        type(self).number_of_instances -= 1
