#!/usr/bin/python3
"""
This module returns your full name.
"""

def say_my_name(first_name, last_name=""):
    """
    This function takes two strings and returns the full name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Defaults to an empty string.

    Raises:
        TypeError: If the input is not a string.

    Returns:
        str: The full name of the person.
    """
    if not isinstance(first_name, str):
        raise TypeError("TypeError: the first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("TypeError: the last_name must be a string")
    else:
        print("My name is", first_name + " " + last_name)
        return first_name + " " + last_name

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")

