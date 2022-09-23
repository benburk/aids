"""
Calculate elementary statistics from a data stream
mean, median, mode

Computing stats can be error prone, to improve numerical accuracy:

sort numbers when computing the mean

"""
import heapq
from collections import defaultdict


class OnlineStats:
    """Computing the mean this way prevents storing large sums."""

    def __init__(self):
        self.n = 0
        self.mean = None

    def add_sample(self, sample: float) -> None:
        # update mean
        if self.mean is None:
            self.mean = sample
        else:
            self.mean = self.mean + (sample - self.mean) / (self.n + 1)

        self.n += 1


# def process(arr):
#     """
#     for median, divide our list into two halves stored in heaps
#     Time: O(nlogn)
#     """
#     # median
#     median = 0
#     min_heap = []
#     max_heap = []

#     # mode
#     counts = defaultdict(int)
#     best = 0
#     mode = 0

#     # mean
#     mean = 0
#     seen = 0

#     for num in arr:
#         # MEAN
#         seen += 1
#         mean = mean + (num - mean) / seen

#         # MODE
#         counts[num] += 1
#         if num != mode and counts[num] > best:
#             mode = num
#             best = counts[num]

#         # MEDIAN
#         small = heapq.heappushpop(min_heap, num)
#         heapq.heappush(max_heap, -small)
#         # if max_heap has more elements, pop an element and add it to min_heap
#         if len(max_heap) > len(min_heap):
#             large = heapq.heappop(max_heap)
#             heapq.heappush(min_heap, -large)

#         if len(max_heap) == len(min_heap):
#             median = 0.5 * (min_heap[0] - max_heap[0])
#         else:
#             median = min_heap[0]

#     print(median)
#     print(mean)
#     print(mode)


def test():
    """run test cases"""
    x = OnlineStats()
    x.add_sample(1.0)
    x.add_sample(3.0)
    assert x.mean == 2.0


if __name__ == "__main__":
    test()
