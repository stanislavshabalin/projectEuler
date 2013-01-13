#!/usr/bin/env python
# -*- coding: utf8 -*-


def main():
    n = 2 ** 1000

    print sum(map(int, list(str(n))))
    return True

if __name__ == "__main__":
    main()
