#!/usr/bin/python3

def element_at(my_list, idx):
    for index in range(len(my_list) - 1):
        if index == idx:
            return my_list[idx]
    return None
