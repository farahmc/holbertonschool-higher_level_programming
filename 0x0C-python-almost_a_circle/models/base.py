#!/usr/bin/python3
"""
A class Base to be the base of other classes in this project
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
