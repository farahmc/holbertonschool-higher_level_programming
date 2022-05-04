#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = []
    for i in my_list:
        if search == i:
            copy_list.append(replace)
        else:
            copy_list.append(i)
    return copy_list
