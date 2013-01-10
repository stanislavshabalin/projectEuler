#!/usr/bin/env python
# -*- coding: utf8 -*- 

a = []
CHUNK = 4

def main():
    f = open('input.txt')
    for line in f:
        a.append( line.rstrip("\n").split(" ") )
    f.close()

    size_str = len(a)
    size_cmn = len(a[0])

    for i in range(0, size_str):
        for j in range(0, size_cmn):
            tryMax( calcTopRight(i, j) )
            tryMax( calcRight(i, j) )
            tryMax( calcDownRight(i, j) )
            tryMax( calcDown(i, j) )

    print tryMax()

    return True

def tryMax(n = 0):
    if not hasattr(tryMax, "mx"):
        tryMax.mx = 0 # kind of a static variable (I should use classes, I know) 
    
    if n > tryMax.mx:
        tryMax.mx = n

    return tryMax.mx

def calcTopRight(i, j):
    if i - CHUNK < 0 or j + CHUNK >= len(a[0]):
        return 0

    mult = 1
    for delta in range(0, CHUNK):
        mult *= int(a[i - delta][j + delta])

    return mult

def calcRight(i, j):
    if j + CHUNK >= len(a[0]):
        return 0

    mult = 1
    for delta in range(0, CHUNK):
        mult *= int(a[i][j + delta])

    return mult

def calcDownRight(i, j):
    if i + CHUNK >= len(a) or j + CHUNK >= len(a[0]):
        return 0

    mult = 1
    for delta in range(0, CHUNK):
        mult *= int(a[i + delta][j + delta])

    return mult


def calcDown(i, j):
    if i + CHUNK >= len(a):
        return 0

    mult = 1
    for delta in range(0, CHUNK):
        mult *= int(a[i + delta][j])

    return mult


if __name__ == "__main__":
    main()