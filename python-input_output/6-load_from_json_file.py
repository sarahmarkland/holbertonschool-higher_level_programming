#!/usr/bin/python3
""" 6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a JSON file

    Args:
        filename (str): Name of the file to read

    Returns:
        obj: Object created from the JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
