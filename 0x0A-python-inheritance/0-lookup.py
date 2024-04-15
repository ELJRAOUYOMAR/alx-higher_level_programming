#!/usr/bin/python3
'''Module for lookup method.'''

def lookup(obg):
    '''Looks up object attributes and methods.
    Args:
        obj (object): the object created from any class. 

    Returns: 
        list: the list of attributes and methods.
    '''
    
    return dir(obj)
        

