#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    n = 0
    for i in range(count):
        n += int(argv[i + 1])
    print(n)
