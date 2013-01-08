#!/usr/bin/env python
# -*- coding: utf8 -*- 

def main():
    TRIPLET_SUM = 1000

    for a in range(1, TRIPLET_SUM / 3):
        for b in range(a + 1, (TRIPLET_SUM - a) / 2): # math for the win
            c = TRIPLET_SUM - a - b
            # (a, b, c) should be already sorted
            if ( a*a + b*b == c*c ):
                print a, b, c
                print a * b * c
                return True

    return False

if __name__ == "__main__":
    main()