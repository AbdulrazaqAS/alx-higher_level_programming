#!/usr/bin/python3

"""Does stuff"""


def inherits_from(obj, a_class):
    """Inherits"""
    return isinstance(obj, a_class) and type(obj) is not a_class
