#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print(f"{(-1 * number) % 10}", end='')
        return(-1 * number) % 10
    else:
        print(f"{number % 10}", end='')
        return(number % 10)
