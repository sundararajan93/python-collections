#!/usr/bin/python3.6

from collections import Counter

set_of_string = "aaaasddddrrrww+++wwcccxxx+++"

my_counter = Counter(set_of_string)

print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common(2))
# print(my_counter.most_common(2)[0][0])

print(list(my_counter.elements()))
