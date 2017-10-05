# -*- coding: utf-8 -*-

from collections import Counter


def number_needed(a, b):
    count_a = Counter(a)
    count_b = Counter(b)

    # first, assume that all letters are needed
    retval = len(a) + len(b)

    # checking the common characters in both strings
    for k in count_a:
        if k in count_b:
            # remove common characters, how many there are
            # don't delete excess characters (must delete in pairs)
            retval -= 2 * min(count_a[k], count_b[k])

            # i.e. A has 3 counts of 'x' and B has 2 counts of 'x'
            # you only remove the 2 counts of 'x' from both A and B
            # because the 3rd 'x' from A is excess
            # result: remove 4 characters in total (2 'x's from both A and B)

    return retval


def main():
    a = input().strip()
    b = input().strip()

    print(number_needed(a, b))

if __name__ == '__main__':
    main()
