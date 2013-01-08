#!/usr/bin/env python
# -*- coding: utf8 -*- 

def main():
    LIMIT = 100

    sum = LIMIT * (LIMIT + 1) / 2
    sum = sum * sum
    for i in range(1, LIMIT + 1):
        sum -= i * i

    print sum
    return True

if __name__ == "__main__":
    main()