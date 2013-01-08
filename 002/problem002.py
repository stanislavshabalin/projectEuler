#!/usr/bin/env python
# -*- coding: utf8 -*- 

def main():
    sum = 0
    for i in fib():
        if i > 4000000:
            break
        
        if 0 == i % 2:
            sum += i

    print sum

    return True

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

if __name__ == "__main__":
    main()