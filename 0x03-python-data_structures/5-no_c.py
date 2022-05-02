#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord('c'): None})
    newer_string = new_string.translate({ord('C'): None})
    return(newer_string)
