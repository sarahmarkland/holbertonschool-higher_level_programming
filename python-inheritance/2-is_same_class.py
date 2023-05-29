#!/usr/bin/python3
"""
module documentation
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class;
        otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is a_class
