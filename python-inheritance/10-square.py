#!/usr/bin/python3
"""
module documentation
"""


class Square(__import__('9-rectangle').Rectangle):
    """
    class Square
    """
    def __init__(self, size):
        """
        function __init__
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        function __str__
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
