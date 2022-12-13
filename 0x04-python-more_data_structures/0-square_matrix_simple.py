#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    res = []
    for i in range(len(matrix)):
        res.append([])
        for j in matrix[i]:
            res[i].append(j ** 2)
    return res
