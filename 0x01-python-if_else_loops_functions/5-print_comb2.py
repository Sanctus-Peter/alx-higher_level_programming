#!/usr/bin/python3
for num in range(100):
    print("{:02d}".format(num), end='\n' if num == 99 else '')
    if num < 99:
        print(", ", end='')
