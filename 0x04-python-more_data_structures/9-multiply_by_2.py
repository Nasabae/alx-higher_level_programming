#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = {}
    for z, value in a_dictionary.items():
        new_dict.update({z: (value * 2)})
    return new_dict
