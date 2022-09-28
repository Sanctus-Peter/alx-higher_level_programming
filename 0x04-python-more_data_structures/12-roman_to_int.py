#!/usr/bin/python3

def roman_to_int(r_str):
    if not isinstance(r_str, str) or r_str is None:
        return None

    rom_var = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    ret = 0
    for i in range(len(r_str)):
        if r_str[i].upper() not in rom_var:
            return 0
        if i == len(r_str) - 1:
            ret += rom_var[r_str[i].upper()]
        elif rom_var[r_str[i].upper()] < rom_var[r_str[i + 1].upper()]:
            ret -= rom_var[r_str[i].upper()]
        else:
            ret += rom_var[r_str[i].upper()]
    return ret
