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

    def area(self):
        """
        Return the area of Rectangle instance
        """
        return (self.width * self.height)

    def display(self):
        """
        Print a representation of a Rectangle instance
        """
        for line in range(self.y):
            print("\n", end="")
        for row in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        Assign an attribute to each argument
        """
        if len(args) != 0:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Return a dictionary representation
        """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}

    @property
    def width(self):
        """ Get the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width, validate value """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height, validate value """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set x, validate value """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set y, validate value """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """
        Return a printable representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
