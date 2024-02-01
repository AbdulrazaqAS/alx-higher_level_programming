#!/usr/bin/python3
"""Stuff"""


def add_attribute(obj, name, value):
    """Stuff"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
