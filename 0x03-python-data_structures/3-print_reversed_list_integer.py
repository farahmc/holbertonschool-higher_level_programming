#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        rev_list = reversed(my_list)
        for i in rev_list:
            print(int(i))
