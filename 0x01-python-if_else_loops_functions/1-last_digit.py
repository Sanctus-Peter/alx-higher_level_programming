#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lDig = number % 10
else:
    lDig = ((-1 * number) % 10) * -1
if lDig > 5:
    print(f"Last digit of {number:d} is {lDig:d} and is greater than 5")
elif lDig == 0:
    print(f"Last digit of {number:d} is {lDig:d} and is 0")
else:
    print(f"Last digit of {number:d} is {lDig:d} and is less than 6 and not 0")
