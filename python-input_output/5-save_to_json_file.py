#!/usr/bin/python3
""" 5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using a JSON
    representation

    Args:
        my_obj (obj): Object to be represented as JSON
        filename (str): Name of the file to write
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
