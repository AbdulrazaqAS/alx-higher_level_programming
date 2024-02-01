#!/usr/bin/python3

from sys import stderr, exc_info


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception:
        print("Exception:", exc_info()[1], file=stderr)
        return None
