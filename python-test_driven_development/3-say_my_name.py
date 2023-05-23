#!/usr/bin/python3
"""2. Say My Name - 3-say_my_name.py"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str): last name

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
