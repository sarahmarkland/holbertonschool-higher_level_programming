#!/usr/bin/python3
""" 4-from_json_string.py"""


def from_json_string(my_str):
    """Function that returns an object (Python data structure) represented
    by a JSON string

    Args:
        my_str (str): JSON string to be represented as an object

    Returns:
        obj: Object represented by the JSON string
    """
    import json
    return json.loads(my_str)
