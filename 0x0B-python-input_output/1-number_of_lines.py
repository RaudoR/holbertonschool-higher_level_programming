#!/usr/bin/python3
def number_of_lines(filename=""):
    '''
    function that returns the number of lines of a text file
    '''
    total_lines = 0

    with open(filename) as f:
        for line in f:
            total_lines += 1
        return total_lines
