#!/usr/bin/python3
# Author - Serwah-Akoto Sandra

z = 0
while z < 8:
    j = z
    while j <= 9:
        if z != j:
            print('{}{}'.format(z, j), end=', ')
            j = j + 1
    z = z + 1
print('{}{}'.format(z, j - 1), sep='')
