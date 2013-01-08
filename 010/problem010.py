#!/usr/bin/env python
# -*- coding: utf8 -*- 

import math

def main():

    LIMIT = 2000000

    print sum( primesList(LIMIT) )

    return True

def primesList(limit):
    res = []
    for n in primes():
        if n >= limit:
            break

        res.append(n)

    return res

def primes():
    yield 2
    
    n = 3
    while True:
        isPrime = True
        limit = int(math.sqrt(n))
        for i in range(2, limit + 1):
            if 0 == n % i:
                isPrime = False
                break

        if isPrime:
            yield n

        n += 2

if __name__ == "__main__":
    main()