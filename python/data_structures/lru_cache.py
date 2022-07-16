"""LRU Cache"""
from collections import deque


class Cache:
    """
    LRU cache implemented using a doubly linked list
    """

    def __init__(self, capacity):
        self.queue = deque(maxlen=capacity)
        self.present = set()

    def refer(self, item):
        """refer to an element and update the cache"""
        if item not in self.present:
            if len(self.queue) == self.queue.maxlen:
                last = self.queue.pop()
                self.present.remove(last)
        else:
            self.queue.remove(item)

        self.queue.appendleft(item)
        self.present.add(item)

    def __repr__(self):
        return str(self.queue)


def test():
    """run test cases"""
    cache = Cache(4)
    cache.refer(1)
    cache.refer(2)
    cache.refer(3)
    cache.refer(1)
    cache.refer(4)
    cache.refer(5)

    print(cache)


if __name__ == "__main__":
    test()
