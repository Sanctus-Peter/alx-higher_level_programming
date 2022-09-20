#!/usr/bin/python3
for num in range(9):
    for var in range(num + 1, 10):
        print(f"{num:d}{var:d}", end='\n' if num == 8 else ', ')
