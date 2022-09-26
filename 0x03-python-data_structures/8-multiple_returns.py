#!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence)
    if (i == 0):
        new_tuple = (i, None)
    else:
        new_tuple = (len(i), sentence[0])
    return new_tuple
