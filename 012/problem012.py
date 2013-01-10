#!/usr/bin/env python
# -*- coding: utf8 -*- 

import math

def main():
    for x in genTriangles():
        if ( getDivisorsCount(x) > 500):
            break

    print x
    return True

def getDivisorsCount(x):
    n = 2 # 1 and x

    if x > 2:
        limit = int(math.sqrt(x))
        for i in range(2, limit):
            if 0 == x % i:
                n += 2

        if limit * limit == x:
            n += 1

    return n

def genTriangles():
    n = 0
    triangle = 0
    while True:
        n += 1
        triangle += n
        yield triangle


if __name__ == "__main__":
    main()