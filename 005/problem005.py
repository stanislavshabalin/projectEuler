#!/usr/bin/env python
# -*- coding: utf8 -*- 

def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19]

    divisors = {}

    for i in range(2, 21):
        for prime in primes:
            if 0 == i % prime:
                div = 1
                tmp = i / prime
                while 0 == tmp % prime:
                    div += 1
                    tmp /= prime

                if prime not in divisors or divisors[prime] < div:
                    divisors[prime] = div

    ans = 1
    for prime, power in divisors.items():
        ans *= prime**power

    print ans

    return True

if __name__ == "__main__":
    main()