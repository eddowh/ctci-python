# -*- coding: utf-8 -*-

from collections import defaultdict


def number_needed(a, b):
    char_count_a = defaultdict(int)
    for c in a:
        char_count_a[c] += 1
    for c in b:
        char_count_a[c] -= 1

    return sum([abs(v) for v in char_count_a.values()])


a = input().strip()
b = input().strip()

print(number_needed(a, b))
