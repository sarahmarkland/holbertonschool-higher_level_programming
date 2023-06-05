#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """if a number is passed in as argument i.e. <Base(12)>, assign
        that number as the public instance attribute id. Else, increment
        __nb_objects and assign the new value to the public instance
        attribute id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
