#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations

comb = combinations([1, 2, 3], 2)

for i in list(comb):
    print (i)