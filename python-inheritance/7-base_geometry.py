#!/usr/bin/python3
"""
module documentation
write a class BaseGeometry
"""


class BaseGeometry:
    """
    class documentation
    """
    def area(self):
        """
        method documentation
        """
        raise Exception(area() is not implemented)

    def integer_validator(self, name, value):
        """
        method documentation
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
