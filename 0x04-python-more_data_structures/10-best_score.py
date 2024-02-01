#!/usr/bin/python3

def best_score(a_dictionary):
    max = 0
    key = ''
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    for i in a_dictionary:
        if a_dictionary[i] > max:
            max = a_dictionary[i]
            key = i
    return key
