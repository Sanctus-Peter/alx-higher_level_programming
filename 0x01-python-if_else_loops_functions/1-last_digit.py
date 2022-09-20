#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    l_digit = number % 10
else:
    l_digit = (-1 * number) % 10
if l_digit > 5:
    print(f"Last digit of {number:d} is {l_digit:d} and is greater than 5")
elif l_digit == 0:
    print(f"Last digit of {number:d} is {l_digit:d} and is 0")
else:
    print(f"Last digit of {number:d} is {l_digit:d} and is less than 6 and not 0")
