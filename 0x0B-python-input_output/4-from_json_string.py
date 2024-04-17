#!/usr/bin/python3
"""Defines a function to return an object represented by a JSON string."""

import json


def from_json_string(my_str):
    """Returns the Python data structure represented by the given JSON string."""
    return json.loads(my_str)
