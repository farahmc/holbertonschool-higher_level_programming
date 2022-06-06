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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write JSON string representation of list_objs to a file
        If list_objs in None, save an empty list
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
            obj.update(**dictionary)
            return obj

        if cls.__name__ == "Square":
            obj = cls(1)
            obj.update(**dictionary)
            return obj
