#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    # (<score>, <weight>)
    total = 0
    w_total = 0
    for i in my_list:
        score, weight = i
        total += (score * weight)
        w_total += weight
    return total / w_total
