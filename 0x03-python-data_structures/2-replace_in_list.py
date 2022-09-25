#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    for index in range(len(my_list) - 1):
        if index == idx:
            my_list[idx] = element
            break
    return my_list
