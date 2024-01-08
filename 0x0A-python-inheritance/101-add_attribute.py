#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""
def add_attribute(obj, att, value):
    
    if not hasattr(obj, "dict"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)