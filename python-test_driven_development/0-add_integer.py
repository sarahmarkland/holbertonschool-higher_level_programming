#!/usr/bin/python3
"""0. Integers Addition - 0-add_integer.py"""


def add_integer(a, b=98):
    ''' 
    Function that takes two integers
    or floats casted to int

    Args:
        a: int
        b: int

    Raises:
        TypeError if a or b is not float or int

    Returns:
        The result of the operation
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("be must be an integer")
    return int(a) + int(b)
