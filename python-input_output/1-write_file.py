#!/usr/bin/python3
""" 1-write_file.py"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8) and returns
    the number of characters written

    Args:
        filename (str): Name of the file to write
        text (str): Text to write in the file

    Returns:
        int: Number of characters written
    """
    if not isinstance(filename, str):
        raise Exception("filename must be a string")
    if not isinstance(text, str):
        raise Exception("text must be a string")
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
