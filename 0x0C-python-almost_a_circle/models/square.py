#!/usr/bin/python3
"""
Function to represent a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Define a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the square

        Arguments:
        size - height and width of square
        x - x
        y - y
        id - id of square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get the size """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assign an attribute to each argument
        """
        if len(args) != 0:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Return a dictionary representation of class Square
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

    def __str__(self):
        """
        Return a string representation
        """
        cls = self.__class__.__name__
        return f"[{cls}] ({self.id}) {self.x}/{self.y} - {self.size}"
