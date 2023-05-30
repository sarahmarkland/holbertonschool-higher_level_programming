#!/usr/bin/python3
""" 11-student.py"""


class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        """__init__ method
        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json method
        Args:
            attrs (list): List of strings of attributes to retrieve
        Returns:
            dict: Dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

    def reload_from_json(self, json):
        """reload_from_json method
        Args:
            json (dict): Dictionary representation of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)