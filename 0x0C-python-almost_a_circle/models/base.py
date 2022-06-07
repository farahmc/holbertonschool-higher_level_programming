#!/usr/bin/python3
"""
A class Base to be the base of other classes in this project
"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """
        Return a list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

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

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                objdict = Base.from_json_string(f.read())
                return [cls.create(**dict) for dict in objdict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize from a Python object to CSV file
        (Write to CSV file)
        """
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            with open(filename, "w") as csv_rec:
                fieldnames = ['id', 'width', 'height', 'x', 'y']
                writer = csv.DictWriter(csv_rec, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
        if cls.__name__ == "Square":
            with open(filename, "w") as csv_sq:
                fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csv_sq, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize from a CSV file to Python object
        (Read from CSV file)
        """
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            try:
                with open(filename, "r") as csv_rec:
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                    reader = csv.DictReader(csv_rec, fieldnames=fieldnames)
                    reader = [dict((k, int(v)) for k, v in dic.items())
                                 for dic in reader]
                return [cls.create(**dic) for dic in reader]
            except IOError:
                return []
        if cls.__name__ == "Square":
            try:
                with open(filename, "r") as csv_sq:
                    fieldnames = ['id', 'size', 'x', 'y']
                    reader = csv.DictReader(csv_sq, fieldnames=fieldnames)
                    reader = [dict((k, int(v)) for k, v in dic.items())
                                 for dic in reader]
                return [cls.create(**dic) for dic in reader]
            except IOError:
                return []
