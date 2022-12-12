#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for col in matrix:
        for row in col:
            if row != col[-1]:
                print('{:d}'.format(row), end=' ')
            else:
                print('{:d}'.format(row), end='')
        print()
