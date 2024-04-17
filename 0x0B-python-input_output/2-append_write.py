#!/usr/bin/python3
"""Defines a function to append a string to a text file and return the number of characters added."""


def append_write(filename="", text=""):
    """Appends the given text to the specified filename and returns the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
