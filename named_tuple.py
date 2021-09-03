#!/usr/bin/python3.6

from collections import namedtuple

P = namedtuple('Point', 'x,y')

pt = P(1,-4)
print(pt.x, pt.y)