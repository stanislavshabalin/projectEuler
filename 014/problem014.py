#!/usr/bin/env python
# -*- coding: utf8 -*-


def main():
    maxLen = 0
    maxNum = 0
    
    for i in range(1, 1000001):
        ln = getChainLen(i)
        if ln > maxLen:
            maxLen = ln
            maxNum = i

    print maxNum
    return True


def getChainLen(n):
    if not hasattr(getChainLen, "cache"):
        getChainLen.cache = {1: 1}

    _n = n
    len = 0
    while (n not in getChainLen.cache):
        if (n % 2):
            n = 3 * n + 1
        else:
            n /= 2
        len += 1

    if _n not in getChainLen.cache:
        getChainLen.cache[_n] = len + getChainLen.cache[n]

    return getChainLen.cache[_n]


if __name__ == "__main__":
    main()
