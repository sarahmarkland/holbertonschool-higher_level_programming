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
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
