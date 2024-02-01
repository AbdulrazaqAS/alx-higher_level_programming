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

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Returns area"""
        return self.__size ** 2
