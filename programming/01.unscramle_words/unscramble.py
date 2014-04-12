#!/usr/bin/env python
from itertools import permutations
import sys

w_list = []


def permute(lst):
    global w_list
    items = []
    for word in lst:
        items.append(list(permutations(word, len(word))))
    for l in items:
        for w in l:
            w_list.append(''.join(w))


if __name__ == '__main__':
    wordlist = []
    found = []
    with open('wordlist.txt', 'r') as fr:
        wordlist = fr.readlines()

    permute(sys.argv[1:])

    for word in w_list:
        if word+'\r\n' in wordlist:
            if word not in found:
                found.append(word)

    print ','.join(found)
