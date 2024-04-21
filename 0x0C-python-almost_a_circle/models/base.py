#!/usr/bin/python3
"""define Base class"""


class Base:
    """Base class"""
    
    __nb_objects = 0

    """Create constructure"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects