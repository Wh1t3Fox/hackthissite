#!/usr/bin/env python
import requests
import json

def is_prime(num):
    return all(num % i for i in xrange(2, num))

def get_string():
    url = 'http://www.hackthissite.org/missions/prog/12/index.php'


def submit(answer):
    url = 'http://www.hackthissite.org/missions/prog/12/index.php'


if __name__ == '__main__':
    get_string()
    primes = []
    composites = []
    chars = []
    output = ''

    with open('string.txt', 'r') as fr:
        string = fr.readline()

    for c in string:
        if c.isdigit():
            c = int(c)
            if c > 1:
                if is_prime(c):
                    primes.append(c)
                else:
                    composites.append(c)
        else:
            if len(chars) < 25:
                chars.append(c)
                output += chr(ord(c)+1)

    total = sum(primes) * sum(composites)
    answer = output+str(total)

    print answer
