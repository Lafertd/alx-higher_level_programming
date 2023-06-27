#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    counter = len(argv) - 1
    if counter != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    s = argv[2]

    if s == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, s, b, add(a, b)))
    elif s == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, s, b, sub(a, b)))
    elif s == "*":
        print("{:d} {:s} {:d} = {:d}".format(a, s, b, mul(a, b)))
    elif s == "/":
        print("{:d} {:s} {:d} = {:d}".format(a, s, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
