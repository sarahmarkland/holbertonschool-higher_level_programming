#!/usr/bin/python3
"""
module documentation
write a class Rectangle that inherits from BaseGeometry
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


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """
    def __init__(self, width, height):
        """
        function __init__
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        function __str__
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        function area
        """
        return self.__width * self.__height
