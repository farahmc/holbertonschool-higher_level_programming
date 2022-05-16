#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (TypeError, ValueError, ZeroDivisionError, IndexError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    return result
