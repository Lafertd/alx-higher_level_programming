#!/usr/bin/python3
"""
This module returs your full name
"""
def say_my_name(first_name, last_name=""):
    """
    this function takes 2 strings and returns the full name

    args:
    first_name: string
    last_name: string

    raises: 
    raise a TypeError if the input is not string

    return:
    retuns the full name of the person

    """
    if first_name is not type(str):
        raise TypeError("TypeError: the first_name must be a string")
    elif last_name is not type(str):
        raise TypeError("TypeError: the last_name must be a string")
    else
    print("My name is", <first name> <last name>)
    return first_name + last_name
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
