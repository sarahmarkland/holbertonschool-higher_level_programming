#!/usr/bin/python3
"""
Return: a list of available attributes and methods of
    an object
"""
def lookup(obj):
    """
    Retrieve the list of attributes and methods associated
    with the given object obj. This func returns sorted list
    of strings containing the names of the attributes and methods.
    """
    return dir(obj)
