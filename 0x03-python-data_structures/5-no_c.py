#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for l in my_string:
        if l != 'c' and l != 'C':
            new_string += l
    return(new_string)
