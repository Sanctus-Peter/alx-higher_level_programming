#!/usr/bin/python3
for char in range(ord("a"), ord("z") + 1):
    if chr(char) == 'e' or chr(char) == 'q':
        continue
    print("{:c}".format(char), end='')
