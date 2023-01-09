#!/usr/bin/python3

def safe_print_divisions(a, b):
    try:
        res = a / b
    except Exception:
        res = None
        pass
    finally:
        print("{:d} / {:d} = {}".format(a, b, res))
        return res
