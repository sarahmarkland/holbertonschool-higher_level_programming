#!/usr/bin/python3
"""Write an empty class that defines a square"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0, area):
        """this initializes a simple square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of the square"""
        return self.__size ** 2
