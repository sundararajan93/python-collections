#!/usr/bin/python3.6
from collections import deque

d = deque()

d.append(1)
d.append(2)
d.append(3)
d.append(4)

print(d)
d.appendleft(5)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.extend([6,7,8,9])
print(d)

d.extendleft([10,11,12])
print(d)


d.rotate(-2)
print(d)

d.rotate(2)
print(d)