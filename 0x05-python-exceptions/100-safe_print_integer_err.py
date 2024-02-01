#!/usr/bin/python3

from sys import stderr, exc_info


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception:
        print("Exception:", exc_info()[1], file=stderr)
        return False
    else:
        return True
