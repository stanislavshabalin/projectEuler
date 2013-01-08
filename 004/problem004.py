#!/usr/bin/env python
# -*- coding: utf8 -*- 

def main():

    max = 0
    threeDigitRange = range(999, 99, -1)
    for a in threeDigitRange:
        for b in threeDigitRange:
            mul = a * b
            if mul > max and isPalindrome(mul):
                max = mul

    print max
    return True

def isPalindrome(num):
    num = str(num)
    return num == "".join(reversed(num))

if __name__ == "__main__":
    main()