def element_at(my_list, idx):
    if idx < 0:
        return(None)
    if idx + 1 > (len(my_list) + 1):
        return(None)
    for i in range(len(my_list)):
        if i == idx:
            return(my_list[i])
