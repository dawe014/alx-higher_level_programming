#!/usr/bin/python3
"""Writing a docstring"""
import math

class MagicClass:
    """Set up the magic"""

    def __init__(self, radius=0):
        """Writing another docstring"""
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = float(radius)

    def area(self):
        """Again with the docstring"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Such docstring"""
        return 2 * math.pi * self.__radius

# Example usage:
# magic_circle = MagicClass(3)
# print(magic_circle.area())
# print(magic_circle.circumference())
