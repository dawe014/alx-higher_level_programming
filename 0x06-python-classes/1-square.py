#!/usr/bin/python3
class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If the provided size is not a positive integer.
        """
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be a positive integer.")
        
        self.__size = size
