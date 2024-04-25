#!/usr/bin/python3

def add_integer(a, b=98):
    try:
        if (isinstance(a, int) or isinstance(a, float)) and \
           (isinstance(b, int) or isinstance(b, float)):
            if isinstance(a, float):
                a = int(a)
            if isinstance(b, float):
                b = int(b)
            return a + b
    except TypeError:
        raise TypeError("a must be an integer")

if __name__ == "__main__":
    a = int(input("enter an integer a: "))
    b = int(input("enter an integer b or the default value will be 98: ") or 98)
    print(add_integer(a, b))
