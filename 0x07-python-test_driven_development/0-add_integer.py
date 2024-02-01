#!/usr/bin/python3

"""Does stuff"""


def add_integer(a, b=98):
    """Adds two integers"""
    if not any((isinstance(a, int), isinstance(a, float))):
        raise TypeError("a must be an integer")
    if not any((isinstance(b, int), isinstance(b, float))):
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)
    return a + b
