#!/usr/bin/python3

"""Stuff"""


class MyInt(int):
    """Int son"""
    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
