#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len1, len2 = len(tuple_a), len(tuple_b)
    res = None
    for idx in (0, 1):
        if len1 >= idx + 1:
            num1 = tuple_a[idx]
        else:
            num1 = 0
        if len2 >= idx + 1:
            num2 = tuple_b[idx]
        else:
            num2 = 0
        if res:
            res = res[0], (num1 + num2)
        else:
            res = num1 + num2,
    return res
