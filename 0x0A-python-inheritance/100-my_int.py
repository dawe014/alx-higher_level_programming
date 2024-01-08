#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""
class MyInt(int):
    """Invert int operators == and !=."""
    def eq(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value
    def ne(self, value):
        """Override != operator with == behavior."""
        return self.real == value