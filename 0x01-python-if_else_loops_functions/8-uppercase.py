#!/usr/bin/python3


def uppercase(str):

    for element in str:
        if element >= 'a' and element <= 'z':
            conv_to_int = (ord(element) - 32)
            conv_to_upper = chr(conv_to_int)
            print(conv_to_upper, end="")
        else:
            print(element, end="")

    print("\n", end="")
