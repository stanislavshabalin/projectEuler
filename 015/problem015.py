#!/usr/bin/env python
# -*- coding: utf8 -*- 

import operator, math

def main():
    FIELD_SIZE = 20

    result = reduce( operator.mul, range(FIELD_SIZE + 1, FIELD_SIZE * 2 + 1), 1) / math.factorial( FIELD_SIZE )

    print result    


if __name__ == "__main__":
    main()