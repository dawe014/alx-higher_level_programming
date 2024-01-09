#!/usr/bin/python3
"""Append To File
"""
def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)