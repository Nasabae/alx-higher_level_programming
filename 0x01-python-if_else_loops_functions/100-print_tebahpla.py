#!/usr/bin/python3
# Author - Serwah-Akoto Sandra

x = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - x)), end="")
    x = 32 if x == 0 else 0
