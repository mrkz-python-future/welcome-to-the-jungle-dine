#!/usr/bin/python2
#encoding=utf-8

from __future__ import print_function

# The form of raising exceptions changed syntax between python2 and
# python3.
# 
# According to http://python-future.org/compatible_idioms.html#raising-exceptions
#
# modify the exceptions raise in order to make it compatible with python3
# hint: only 2 lines of code require to be changed.

def do_something():
    raise Exception, "Nothing was done ;-("


def main():
    """main function, no code from this should be modified"""
    try:
        do_something()
    except:
        print("catched the exception!")


if __name__ == "__main__":
    main()
