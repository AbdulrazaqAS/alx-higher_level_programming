#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    copy = []
    for idx in my_list:
        if idx % 2 == 0:
            copy.append(True)
        else:
            copy.append(False)
    return copy
