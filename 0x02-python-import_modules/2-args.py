#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenOfArg = len(argv)

    if lenOfArg == 1:
        print("0 arguments.")
    elif lenOfArg == 2:
        print("{} argument:".format(lenOfArg - 1))
    else:
        print("{} arguments:".format(lenOfArg - 1))
    for index, var in enumerate(argv):
        if index == 0:
            continue
        print("{}: {}".format(index, var))
