#!/usr/bin/python3
# 2-square.py
"""A module that defines a square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initialize the square class.
        
        Args:
            size: Represents the size of the square.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
