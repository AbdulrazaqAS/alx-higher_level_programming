#!/usr/bin/python3

def element_at(my_list, idx):
    l = len(my_list);
    if idx >= l:
        return None
    if my_list[idx] < 0:
        return None
    else:
        return my_list[idx]
