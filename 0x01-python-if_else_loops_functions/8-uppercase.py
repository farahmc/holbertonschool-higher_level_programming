#!/usr/bin/python3


def uppercase(str):

    for i in str:
        if i >= 'a' and i <= 'z':
            conv_to_int = ord(i) - 32
            conv_to_upper = chr(conv_to_int)
        print(i, end="")

    print("")
