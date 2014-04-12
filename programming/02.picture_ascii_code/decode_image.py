#!/usr/bin/env python
from PIL import Image

morse = {
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-.-': '.',
    '--..--': ',',
    '..--..': '?'
}

if __name__ == '__main__':

    img = Image.open('download.png')
    width, height = img.size
    im = img.load()

    chars = []
    tmp = 0
    for y in xrange(height):
        for pos, x in enumerate(xrange(width)):
            if y == 0:
                pos = pos
            else:
                pos = pos+1*100*y

            if im[x,y] == 1:
                chars.append(chr(pos-tmp))
                tmp = pos
    code =  ''.join(chars).split()

    print ''.join([morse[char] for char in code])
