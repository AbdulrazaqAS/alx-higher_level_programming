#!/usr/bin/python3
"""Does stuff"""


def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        for j in range(i):
            a = 1
            for k in triangle[i - 1]:
                row.append(a + k)
                a = k
        triangle.append(row)
