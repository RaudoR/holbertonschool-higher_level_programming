#!/usr/bin/python3
"""
This module prints square
"""


def print_square(size):


    """
    prints square of given size
    Raises:
        TypeError: if size is not int
        ValueError: if size is less than 0
    """


    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
