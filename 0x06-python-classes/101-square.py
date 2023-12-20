#!/usr/bin/python3
"""My square module."""

class Square:
    """Define a Square."""

    def __str__(self):
        """Teach Python to print the square my way"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with this
        Args:
            size: a side of square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property of the length of a side of square
        Raises:
            TypeError: if size is not an int.
            ValueError: if size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square
        Args:
            value: the size
        Raises:
            TypeError: if value is not int
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Property of the position of square
        Raises:
            TypeError: if value != tuple of 2 ints >= 0.
        Returns: the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position
        Args:
            value: where
        Raises:
            TypeError: if not tuple, ints, positive
        Returns: the position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """The area of square
        Returns:
            size * size
        """
        return self.size * self.size

    def pos_print(self):
        """Returns the printed square with position"""
        pos = ""
        if not self.size:
            return "\n"
        for _ in range(self.position[1]):
            pos += "\n"
        for _ in range(self.size):
            for _ in range(self.position[0]):
                pos += " "
            pos += "#" * self.size + "\n"
        return pos

    def my_print(self):
        """Print square."""
        print(self.pos_print(), end="")

# Example usage:
# square = Square(3, (1, 2))
# print(square)
# square.my_print()
