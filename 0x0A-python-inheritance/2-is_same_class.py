#!/usr/bin/python3
'''
python function to check instance of object
'''

def is_same_class(obj, a_class):
    '''
    check if instance is the same
    '''
    return issubclass(a_class, type(obj))
