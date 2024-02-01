#!/usr/bin/python3

"""Magic Stuff
Proudly coded by me without any form of assistance :)
"""

import math


class MagicClass:
    """Magic class"""
    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
