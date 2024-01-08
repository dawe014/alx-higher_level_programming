#!/usr/bin/python3
def add_attribute(obj, attr, value):
    """Adds a new attribute to an object"""
    if isinstance(obj, (int, float, complex, bool, str, tuple, range,
                        frozenset, bytes)):
        raise TypeError("can't add new attribute")
    obj.__setattr__(attr, value)