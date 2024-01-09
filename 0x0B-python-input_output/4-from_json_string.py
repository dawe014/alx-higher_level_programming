#!/usr/bin/python3
from json import loads
"""
From JSON String To Object Module
"""
def from_json_string(my_str):
    """
    returns an object represented by a JSON string
    """
    return loads(my_str)