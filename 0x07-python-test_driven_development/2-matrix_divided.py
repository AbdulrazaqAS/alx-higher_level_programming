#!/usr/bin/python3

"""Does Stuff"""


def matrix_divided(matrix, div):
    """Divides all element of matrix by div"""
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not all(type(row) is list for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not all(isinstance(i, int) or isinstance(i, float)
               for row in matrix for i in row):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    rows = [len(row) for row in matrix]
    for i in range(1, len(rows)):
        if rows[i] != rows[i - 1]:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    for row in matrix:
        new_row = [round(i / div, 2) for i in row]
        new.append(new_row)

    return new
