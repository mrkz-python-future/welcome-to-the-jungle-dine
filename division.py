#!/usr/bin/python3
#encoding=utf-8

from __future__ import print_function

# The division operation was changed between python2 and python3
# 
# In python2 an operation like 3/2 will return 1, while performing
# the same operation in python3 will result in 1.5.
# According to http://python-future.org/compatible_idioms.html#division
#
# modify the division function to work as integer division
# hint: only 2 lines of code require to be changed.

def division(a, b):
    """This function returns the division of the given 2 numeric values."""
    if b != 0:
        return a//b

def main():
    """main function, no code from this should be modified"""
    result = division(3,2)
    if result != 1:
        print("3/2 is not correct! (expecting 1, recieved {0})".format(result))
    else:
        print("Result: {0}".format(result))

if __name__ == "__main__":
    main()
