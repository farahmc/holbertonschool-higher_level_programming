#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0]
    if sentence is None:
        return(0, None)
    return(length, first_char)
