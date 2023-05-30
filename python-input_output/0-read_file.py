#!/usr/bin/python3
""" 0-read_file.py
Module that defines a function that reads a text file (UTF8) and prints
it to stdout
"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): Name of the file to read

    Raises:
        Exception: If the object is not a string or if it can't be
        decoded
    """
    if not isinstance(filename, str):
        raise Exception("filename must be a string")
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
