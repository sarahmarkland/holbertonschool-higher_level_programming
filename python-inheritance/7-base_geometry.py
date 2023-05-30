#!/usr/bin/python3
"""
module documentation
write a class BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        function area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function integer_validator
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
