#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    copy = my_list[:]
    if idx >= length or idx < 0:
        return copy
    copy[idx] = element
    return copy
