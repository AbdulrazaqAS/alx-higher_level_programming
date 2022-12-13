#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {'I' : 1, 'II' : 2, 'III' : 3, 'IV' : 4, 'V' : 5,
            'VI' : 6, 'VII' : 7, 'VIII' : 8, 'IX' : 9, 'X' : 10,
            'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    res, last = 0, 0
    for i in roman_string:
    if roman[i] > last:
            res += (roman[i] - last - last)
        else:
            res += roman[i]
        last = roman[i]
    return res
