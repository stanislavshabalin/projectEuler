#!/usr/bin/env python
# -*- coding: utf8 -*- 

words = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

wordsLen = {}

def main():
    # calculating lengths from words
    for k, word in words.items():
        wordsLen[k] = len(word)

    lenSum = 0
    print sum(map(numberLen, range(1, 1001)))

    return True

'''Works only on numbers between 1 and 1000'''
def numberLen(num):
    # hundreds: three hundred and ~ ones[] + 7 + 3 = ones + 10

    if not (1 <= num <= 1000):
        raise ValueError()

    if ( num == 1000 ):
        return len("onethousand")

    numLen = 0

    hundreds = num / 100
    if ( 0 != hundreds ):
        numLen += wordsLen[hundreds] + 10 # see comment above
        if 0 == num % 100:
            return numLen - 3 # no " and"

    num %= 100

    if ( num <= 19 ):
        numLen += wordsLen[num]
        return numLen
    else:
        numLen += wordsLen[num - (num % 10)]

    numLen += wordsLen[num % 10]

    return numLen

if __name__ == "__main__":
    main()
