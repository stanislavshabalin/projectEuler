#!/usr/bin/env python
# -*- coding: utf8 -*-


def main():
    numbers = []

    f = open("input.txt")
    for line in f:
        line = line.rstrip("\n")

        if not numbers:
            numbers = [[] for i in range(len(line))]

        i = 0
        for n in reversed(line):
            numbers[i].append(int(n))
            i += 1
    f.close()

    result = ""
    carry = 0
    for nums in numbers:
        carry += sum(nums)
        result = str(carry % 10) + result
        carry /= 10

    result = str(carry)[::-1] + result
    print result[:10:]

    return True

if __name__ == "__main__":
    main()
