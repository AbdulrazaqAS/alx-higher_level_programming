#!/usr/bin/python3
"""Does stuff"""


def append_write(filename="", text=""):
    """Does stuff"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

