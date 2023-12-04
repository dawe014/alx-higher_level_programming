#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return none
    elif idx >= len(my_list):
        return none
    else:
        new_list=my_list.copy()
        new_list[idx]=element
        return new_list