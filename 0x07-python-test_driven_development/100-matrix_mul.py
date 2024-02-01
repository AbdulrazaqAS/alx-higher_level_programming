#!/usr/bin/python3
"""Matrix Multiplication Module M3"""


def matrix_mul(m_a, m_b):
    """Does stuff"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all((isinstance(m_a_ele, list) for m_a_ele in m_a)):
        raise TypeError("m_a must be a list of lists")
    if not all((isinstance(m_b_ele, list) for m_b_ele in m_b)):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or not all((len(row)) != 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or not all((len(row)) != 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    if not all((isinstance(ele, int) or isinstance(ele, float)
                for row in m_a for ele in row)):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float)
                for row in m_b for ele in row)):
        raise TypeError("m_b should contain only integers or floats")

    if not all((len(row) == len(m_a[0]) for row in m_a)):
        raise TypeError("each row of m_a must be of the same size")
    if not all((len(row) == len(m_b[0]) for row in m_b)):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):  # if  m_a cols != m_b rows
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for i in range(len(m_a)):  # num of rows in new matrix
        new_row = []
        for j in range(len(m_b[0])):  # m_b cols
            row_ele = 0
            for k in range(len(m_a[0])):
                row_ele += (m_a[i][k] * m_b[k][j])
            new_row.append(row_ele)
        new_matrix.append(new_row)
    return new_matrix
