#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0]
    if sentence is not None:
        return(length, first_char)
    else:
        return(length, None)
