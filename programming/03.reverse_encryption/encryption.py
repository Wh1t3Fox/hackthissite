#!/usr/bin/env python
from hashlib import md5

def evalCrossTotal(md5):
    return str(sum(int('0x0'+c, 16) for c in md5.split()))
    
def encryptString(string, password):
    md5pass = md5(password).hexdigest()
    md5total = evalCrossTotal(md5pass)
    encrypt_values = []
    for i in xrange(len(string)):
         encrypt_values.append(str(ord(string[i]) + int('0x0'+md5pass[i%32],16) - int(md5total)))
         md5total = evalCrossTotal(md5(string[:i+1]).hexdigest()[:16] + md5(md5total).hexdigest()[:16])
    return ' '.join(encrypt_values)
    
if __name__ == '__main__':
    with open('serials_example.txt', 'r') as fr:
        string = fr.readlines()
    print encryptString(''.join(string), 'ok')
