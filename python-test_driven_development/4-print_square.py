#!/usr/bin/python3
"""3. Print square - Write a function that prints a square with the character #."""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): size of the square

    Raises:
        TypeError: if size is not an int
        ValueError: if size is less than 0

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be > 0")

    for i in range(size):
        print("#" * size)
