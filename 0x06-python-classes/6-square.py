#!/usr/bin/python3
"""My square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a Square
        Args:
            size: length of a side of Square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    def __str__(self):
        return self.pos_print()

    @property
    def size(self):
        """The property of size as the length of a side of Square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Property of the coordinates of this Square
        Raises:
            TypeError: if value is not a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of this Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get the area of a Square
        Returns: The size squared
        """
        return self.size ** 2

    def pos_print(self):
        """Returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for _ in range(self.position[1]):
            pos += "\n"
        for _ in range(self.size):
            pos += " " * self.position[0] + "#" * self.size + "\n"
        return pos

    def my_print(self):
        """Print the square in position"""
        print(self.pos_print(), end='')


# Example usage:
# square = Square(3, (1, 2))
# print(square)
# square.my_print()
