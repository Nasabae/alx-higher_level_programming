#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    sum = 0
    for z in range(1, length):
        num = int(sys.argv[z])
        sum += num
    print("{}".format(sum))
