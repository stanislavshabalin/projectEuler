#!/usr/bin/env python
# -*- coding: utf8 -*- 

import math
import itertools

def main():
    NUMBER = 600851475143

    limit = int( math.sqrt(NUMBER) )
    
    rng = range(2, limit + 1)
    sieve = dict( itertools.izip( rng, rng ) )
    primes = []

    while True:
        if not sieve:
            break

        next = sieve.iterkeys().next()

        for i in range(next, limit + 1, next):
            if i in sieve:
                del sieve[i]

        primes.append(next)

    for prime in reversed(primes):
        if 0 == NUMBER % prime:
            print prime
            break

    return True


if __name__ == "__main__":
    main()