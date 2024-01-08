#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
import importlib

module_name = '7-base_geometry'
module = importlib.import_module(module_name)

# Now you can access the BaseGeometry class
BaseGeometry = module.BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height