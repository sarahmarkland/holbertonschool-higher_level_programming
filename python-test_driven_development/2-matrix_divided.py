#!/usr/bin/python3
"""1. Matrix Divided - 2-matrix_divided.py"""

def matrix_divided(matrix, div):
    '''
    Function that divides all elements of matrix
    by given number

    Args:
        matrix
        div

    Raises:
        TypeError if matrix is not a list of lists
        of integers or floats
        TypeError if each row of the matrix must is
        not same size
        TypeError if div is not number (int/flaot)
        TypeError if div is 0

    Returns:
        A new matrix
    '''
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
