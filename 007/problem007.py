#!/usr/bin/env python
# -*- coding: utf8 -*- 

import math

def main():
    PRIME_POSITION = 10001

    i = 0
    for n in primes():
        i += 1
        if i == PRIME_POSITION:
            print n
            break

    return True

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