#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    tmp = my_list[0]
    for idx in my_list:
        if idx > tmp:
            tmp = idx
    return tmp
