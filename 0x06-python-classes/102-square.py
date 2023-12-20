#!/usr/bin/python3
"""My square module"""

class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Create a Square
        Args: size: length of a side of Square
        """
        self.__size = size

    @property
    def size(self):
        """The property of size as the length of a side of Square
        Raises:
            TypeError: if size is not an int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Get the area of a Square
        Returns: The size squared
        """
        return self.size * self.size

    def le(self, other):
        return self.area() <= other.area()

    def lt(self, other):
        return self.area() < other.area()

    def ge(self, other):
        return self.area() >= other.area()

    def ne(self, other):
        return self.area() != other.area()

    def gt(self, other):
        return self.area() > other.area()

    def eq(self, other):
        return self.area() == other.area()

# Example usage:
# square1 = Square(3)
# square2 = Square(2)
# print(square1.le(square2))
# print(square1.lt(square2))
# print(square1.ge(square2))
# print(square1.ne(square2))
# print(square1.gt(square2))
# print(square1.eq(square2))
