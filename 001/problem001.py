#!/usr/bin/env python
# -*- coding: utf8 -*- 

LIMIT = 1000

def main():
    print sum(dividers(3)) + sum(dividers(5)) - sum(dividers(15))
    return True

def dividers(num):
    return range(num, LIMIT, num)

if __name__ == "__main__":
    main()