#!/usr/bin/python3

def uniq_add(my_list=[]):
    tmp = 0
    for i in set(my_list):
        tmp += i
    return (tmp)
