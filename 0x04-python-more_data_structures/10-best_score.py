#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        return(sorted(a_dictionary, key=a_dictionary.get)[-1])
    return None
