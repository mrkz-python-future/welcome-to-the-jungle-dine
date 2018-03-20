#!/usr/bin/python3
#encoding=utf-8

# THE FINAL CHALLANGE: Work as a true team and each member should
# integrate their changes of their own task in this code that
# compiles all the changes in a single source code!
#
# What will be evaluated:
#
# * each change should integrated by the team member that commited
#   the individual fix of the other python mini-challanges.
#
# * code should be python-future ready! (Python3 compatible)

import Queue
import argparse
import sys

# The division operation was changed between python2 and python3
#
# In python2 an operation like 3/2 will return 1, while performing
# the same operation in python3 will result in 1.5
#
# commit change: modify the division function to work properly with python3.
def division(a, b):
    """This function returns the division of the given 2 numeric values."""
    if b != 0:
        return a//b

# The puts function will print the given message on screen, but this is python2
# format, change it to work properly on python3
#
# commit change: modify the puts function to work properly with python3
def puts(message):
    print (message)

# The naming of the Queue library on python has changed between
# python2 and python3, according to
# http://python-future.org/compatible_idioms.html#queue
# modify the required lines of code to make this code to work with
# python3.

# commit change: modify the queue import and instance call to work properly
# with python3

def use_queue():
    """perform some queue operations"""
    q = Queue.Queue()
    for i in range(10):
        q.put_nowait(i)
    while q.qsize() > 0:
        element = q.get_nowait()
        sys.stdout.write("poping out from queue: {0}\n".format(element))


# The form of raising exceptions changed syntax between python2 and
# python3.
#
# According to http://python-future.org/compatible_idioms.html#raising-exceptions
#
# commit change: modify the exceptions raise in order to make it compatible with python3

def do_something():
    raise valueError( "Nothing was done ;-(")


def main():
    """main function, no code from this should be modified"""
    # evaluate code is running with python3
    version = sys.version_info[0]
    if version != 3:
        sys.stdout.write("code is not running with python3!\n")
    else:
        sys.stdout.write("code is running with python3!\n")

    # evaluate the print statement
    puts("print works corretly from python3!")

    # evaluate the queue correctness
    use_queue()

    # evaluate the division
    result = division(3,2)
    if result != 1.5:
        puts("3/2 is not correct! (expecting 1.5, recieved {0})\n".format(result))
    else:
        puts("Division is correct!\n")

    # evaluate the exception raise
    try:
        do_something()
    except:
        print("catched the exception!")


if __name__ == "__main__":
    main()
