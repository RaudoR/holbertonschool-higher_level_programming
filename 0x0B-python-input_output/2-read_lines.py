#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    '''
    Write a function that reads n lines of a text file (UTF8) and prints it
    '''
    with open(filename) as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        for line_num in range(nb_lines):
            print(f.readline(), end='')
