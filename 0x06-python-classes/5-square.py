#!/usr/bin/python3
# 5-square.py
"""A module that defines a square """

class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: Represents the size of the square defined
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate the area of the square
        Returns: The square of the size
        """

        return self.__size ** 2

    def my_print(self):
        """Print the square in #"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

# Example usage:
# square = Square(3)
# square.my_print()