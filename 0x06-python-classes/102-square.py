#!/usr/bin/python3

"""Square Module
Does nothing
"""


class Square:
    """Square class
    pass
    """
    def __init__(self, size: int = 0):
        """init
        init

        Args:
            size (int): size
        """
        self.__size = size

    def area(self):
        """Returns area"""
        return self.__size ** 2

    def __get_size(self):
        """size getter"""
        return self.__size

    def __set_size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()

    size = property(__get_size, __set_size)
