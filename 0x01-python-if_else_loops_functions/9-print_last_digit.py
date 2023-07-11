#!/usr/bin/python3
# Author - Serwah-Akoto Sandra

def print_last_digit(number):
    if number < 0:
        number = number * -1
    last = number % 10
    print(last, end='')
    return(last)
