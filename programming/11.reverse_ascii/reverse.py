#!/usr/bin/env python
import sys




if __name__ == '__main__':
    string = '30,32,23,31,5,5,'
    shift = -30
    string = string.split(string[-1])
    string.remove('')

    output = ''.join([chr(int(c) - int(shift)) for c in string])
    print output
