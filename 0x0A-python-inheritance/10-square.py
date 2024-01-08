#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
import importlib

module_name = '9-rectangle'
module = importlib.import_module(module_name)
Rectangle = module.Rectangle
class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
