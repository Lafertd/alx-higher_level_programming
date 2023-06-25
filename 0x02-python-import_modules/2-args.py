#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{:d} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
        print("1: {} ".format(argv[1]))
    else:

        print("{:d} arguments:".format(len(argv) - 1))
        for index, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(index, arg))

