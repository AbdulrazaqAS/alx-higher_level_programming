#!/usr/bin/python3

"""Does stuff"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Stuff"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
