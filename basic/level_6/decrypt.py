#!/usr/bin/env python

import sys


def decrypt(code):
    chars = []
    for pos,c  in enumerate(code):
        chars.append(chr(ord(c)-pos))
    print ''.join(chars)


if __name__ == '__main__':
    decrypt(sys.argv[1])

