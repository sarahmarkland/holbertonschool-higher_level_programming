#!/usr/bin/python3
""" 3-to_json_string.py"""


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object (string)

    Args:
        my_obj (obj): Object to be represented as JSON

    Returns:
        str: JSON representation of the object
    """
    import json
    return json.dumps(my_obj)
