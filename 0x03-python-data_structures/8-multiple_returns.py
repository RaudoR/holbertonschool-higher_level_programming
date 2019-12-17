#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        f_letter = None
    else:
        f_letter = sentence[0]
    return len(sentence), f_letter
