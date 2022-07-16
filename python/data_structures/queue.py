"""
Queue implementation

Links:
    https://docs.python.org/3/library/collections.html#deque-objects
"""
from collections import deque


class Queue:
    """Queue implementation"""

    def __init__(self, maxlen=None):
        self._deque = deque(maxlen=maxlen)

    def __len__(self):
        return len(self._deque)

    def is_empty(self):
        """Return whether the queue contains any items"""
        return not self._deque

    def enqueue(self, item):
        """Add an item to the queue"""
        self._deque.append(item)

    def dequeue(self):
        """Pop an item from the queue"""
        return self._deque.popleft()
