"""
Calculate elementary statistics from a data stream
mean, median, mode
"""
import heapq
from collections import defaultdict


def process(arr):
    """
    for median, divide our list into two halves stored in heaps
    Time: O(nlogn)
    """
    # median
    median = 0
    min_heap = []
    max_heap = []

    # mode
    counts = defaultdict(int)
    best = 0
    mode = 0

    # mean
    mean = 0
    seen = 0

    for num in arr:
        # MEAN
        seen += 1
        mean = mean + (num - mean) / seen

        # MODE
        counts[num] += 1
        if num != mode and counts[num] > best:
            mode = num
            best = counts[num]

        # MEDIAN
        small = heapq.heappushpop(min_heap, num)
        heapq.heappush(max_heap, -small)
        # if max_heap has more elements, pop an element and add it to min_heap
        if len(max_heap) > len(min_heap):
            large = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -large)

        if len(max_heap) == len(min_heap):
            median = 0.5 * (min_heap[0] - max_heap[0])
        else:
            median = min_heap[0]

    print(median)
    print(mean)
    print(mode)


def test():
    """run test cases"""
    arr = [1, 2, 3, 2, 5, 4, 3, 3]
    process(arr)


if __name__ == "__main__":
    test()
