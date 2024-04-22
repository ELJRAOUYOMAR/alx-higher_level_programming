#!/usr/bin/python3
"""define Base class"""
import json


class Base:
    """Base class"""
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructure"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)