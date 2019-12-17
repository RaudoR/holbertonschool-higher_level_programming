#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for iterator in my_string:
        if iterator is not 'c' and iterator is not 'C':
            new += iterator
    return new
