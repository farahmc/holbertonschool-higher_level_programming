#!/usr/bin/python3
"""
A class Base to be the base of other classes in this project
"""


class Base:
    """
    Defines a base model

    Attributes:
    __nb_objects - number of instantiated objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialise the class

        Arguments:
        id - value of type int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
