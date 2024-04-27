#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The addition of `a` and `b`.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":

    import doctest
    doctest.testfile("add_integer.txt")
