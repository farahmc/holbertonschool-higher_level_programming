#!/usr/bin/python3


def print_last_digit(number):
    number_string = repr(number)
    last_number_string = number_string[-1]
    last_number = int(last_number_string)
    print(f"{last_number}", end="")

    return(last_number)
