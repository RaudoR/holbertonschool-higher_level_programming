#!/usr/bin/python3
def read_file(filename=""):
    '''
    Read the file inputed
    '''
    with open(filename) as f:
        for line in f:
            print(line, end="")
