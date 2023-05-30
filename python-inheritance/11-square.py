#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size):
        """
        function __init__
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        """
        function area
        """
        return self.__size ** 2

    def __str__(self):
        """
        function __str__
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
