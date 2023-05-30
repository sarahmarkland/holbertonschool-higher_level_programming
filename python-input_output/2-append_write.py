#!/usr/bin/python3
""" 2-append_write.py"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str): Name of the file to append
        text (str): Text to append in the file

    Returns:
        int: Number of characters added
    """
    if not isinstance(filename, str):
        raise Exception("filename must be a string")
    if not isinstance(text, str):
        raise Exception("text must be a string")
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
