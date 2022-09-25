#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy = my_list[:]
    for index in range(len(copy) - 1):
        if index == idx:
            copy[idx] = element
            break
    return copy
