#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    if (roman_string is None or type(roman_string) == int):
        return 0
    res, last = 0, 0
    for i in roman_string:
        if roman[i] > last:
            res += (roman[i] - last - last)
        else:
            res += roman[i]
        last = roman[i]
    return res
