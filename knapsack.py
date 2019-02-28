from random import randint
from fractions import gcd
from modtools import *

def decrypt(c, w, r, q):
    plaintext = [0]*len(w)
    ctext = (c * modinv(r, q)) % q

    while(ctext > 0):
        y = max(x for x in w if x <= ctext)
        ctext -= y
        plaintext[w.index(y)] = 1

    return plaintext

def encrypt(m, B):
    return sum([m[i] * B[i] for i in range(len(m))])

def binarize(m):
    return [int(i) for i in "{:08b}".format(m)]

def generate_keys(n):
    w = [randint(1, 10)]
    multiplier = randint(2, 4)
    for i in range(n - 1):
        w += [randint(sum(w), multiplier*sum(w))]

    q = randint(sum(w), multiplier*sum(w))
    r = randint(1, q)

    while gcd(q, r) != 1:
        r = randint(0, q)

    B = [(w[i] * r) % q for i in range(len(w))]
    
    return B, w, q, r

if __name__ == "__main__":
    B, w, q, r = generate_keys(8)
    m = binarize(97)
    c = encrypt(m, B)
    p = decrypt(c, w, r, q)
    print(c, p)
