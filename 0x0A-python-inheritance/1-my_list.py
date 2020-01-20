#!/usr/bin/python3
'''
python class to inherit from list
'''
class MyList(list):
    '''
    inheritance
    '''
    def print_sorted(self):
        print(sorted(self))
