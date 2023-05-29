#!/usr/bin/python3
"""
Module documentation:
Write a function that returns True if the object is an
instance of, or if the object is an instance of a class
that inherited from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of, or if the object is
        an instance of a class that inherited from, the specified
        class; otherwise, False.
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
