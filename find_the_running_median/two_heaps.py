# -*- coding: utf-8 -*-

from heapq import heappush, heappop


def main():
    n = int(input().strip())
    a_i = 0

    # create one min heap, one max heap
    max_heap = []
    min_heap = []
    median = 0

    for a_i in range(n):
        a_t = int(input().strip())

        # IMPORTANT: check for balance
        # this property is what allows us to infer the median
        assert(abs(len(max_heap) - len(min_heap)) <= 1)

        # if new number is greater than median, push to min_heap
        if a_t > median:
            if len(max_heap) < len(min_heap):
                heappush(max_heap, -heappop(min_heap))
            heappush(min_heap, a_t)

        # if new number is less than median, push to max_heap
        elif a_t < median:
            if len(max_heap) > len(min_heap):
                heappush(min_heap, abs(heappop(max_heap)))
            heappush(max_heap, -a_t)

        # if new number is equal to median, push to the heap that has less elements
        # if they are equal in size, arbitrarily choose a heap (doesn't matter)
        else:
            if len(max_heap) < len(min_heap):
                heappush(max_heap, -a_t)
            elif len(max_heap) >= len(min_heap):
                heappush(min_heap, a_t)

        # if heaps are not balanced, take the min / max from the larger-sized
        # heap
        if len(max_heap) > len(min_heap):
            median = abs(max_heap[0])
        elif len(max_heap) < len(min_heap):
            median = min_heap[0]

        # if heap sizes are balanced, take the min and max
        # from the min_heap and max_heap respectively
        # then,compute the average of those values
        else:
            median = (abs(max_heap[0]) + min_heap[0]) / 2

        # output pythonically
        print("{:.1f}".format(median))


if __name__ == '__main__':
    main()
