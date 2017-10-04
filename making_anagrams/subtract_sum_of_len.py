# -*- coding: utf-8 -*-

from collections import Counter


def number_needed(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    retval = len(a) + len(b)
    for k in count_a:
        if k in count_b:
            retval -= 2 * min(count_a[k], count_b[k])
    return retval


a = input().strip()
b = input().strip()

print(number_needed(a, b))
