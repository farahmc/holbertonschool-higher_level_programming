#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return(None)

    copy_list = list(my_list)
    for i in copy_list:
        if i % 2 == 0:
            copy_list[i] = True
        else:
            copy_list[i] = False
    return(copy_list)
