#!/usr/bin/python3

"""Does stuff"""


class BaseGeometry:
    """BaseGeo"""
    def area(self):
        """Raise"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
