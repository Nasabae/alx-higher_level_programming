#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for z in my_string:
        if z != 'c' and z != 'C':
            new_str = new_str + z
    return new_str
