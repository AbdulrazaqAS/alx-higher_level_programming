#!/usr/bin/python3
"""Square Module
Square stuffs
"""


class Square:
    """Square class
    pass
    """
    def __init__(self, size: int = 0, position=(0, 0)):
        """init
        init

        Args:
            size (int): size
            position (tuple); position
        """
        self.__size = size
        self.__position = position
    
    @position.setter
    def position(self, value):
        print("Here")
        if not isinstance(value, tuple) or not isinstance(value[0], int) or\
                not isinstance(value[1], int) or len(value) != 2 or value[0]\
                < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    @property
    def position(self):
        return self.__position
 
    def area(self):
        """Returns area"""
        return self.__size ** 2

    def my_print(self):
        """my print"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__postion[0] > 0:
                    print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    def __get_size(self):
        """size getter"""
        return self.__size

    def __set_size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    
    size = property(__get_size, __set_size)
