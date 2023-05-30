#!/usr/bin/python3
""" 8-class_to_json.py"""


def class_to_json(obj):
    """Function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object

    Args:
        obj (obj): Object to be serialized

    Returns:
        dict: Dictionary representation of the object
    """
    return obj.__dict__
