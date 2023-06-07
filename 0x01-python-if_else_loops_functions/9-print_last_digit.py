#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        lastd = number % 10
    else:
        lastd = (number % -10) * -1
    print("{}".format(lastd), end="")
    return(lastd)
