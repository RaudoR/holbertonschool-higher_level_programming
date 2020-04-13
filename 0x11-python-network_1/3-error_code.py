#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8).
'''
from urllib import request, error
from sys import argv
if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("utf8"))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
