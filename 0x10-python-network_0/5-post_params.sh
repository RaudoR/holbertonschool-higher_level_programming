#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL
curl -s POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
