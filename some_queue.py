#!/usr/bin/python3
#encoding=utf-8

from __future__ import print_function
import queue

# The naming of the Queue library on python has changed between
# python2 and python3, according to 
# http://python-future.org/compatible_idioms.html#queue
# modify the required lines of code to make this code to work with
# python3.

# hint: only 3 lines of code require to be changed.

def use_queue():
    """perform some queue operations"""
    q = queue.Queue()
    for i in range(10):
        q.put_nowait(i)
    while q.qsize() > 0:
        element = q.get_nowait()
        print("poping out from queue: {0}".format(element))


def main():
    """main function, no code from this should be modified"""
    use_queue()


if __name__ == "__main__":
    main()
