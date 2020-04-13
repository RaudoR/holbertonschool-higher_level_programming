#!/usr/bin/python3
'''script to fetch the url https://intranet.hbtn.io/status'''

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
