from typing import TypeVar

T = TypeVar("T")


class CircularQueue:
    def __init__(self, capacity: int) -> None:
        self.buffer = [0] * capacity
        self.head = 0
        self.tail = 0
        self.capacity = capacity
        self.size = 0

    def __len__(self) -> int:
        """Returns the number of items in the queue."""
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def push_back(self, item: T) -> None:
        """Adds an item to the back of the queue."""
        if self.is_full():
            self.pop_front()

        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def push_front(self, item) -> None:
        """Adds an item to the front of the queue."""
        if self.is_full():
            self.pop_back()
        self.head = (self.head - 1) % self.capacity
        self.buffer[self.head] = item
        self.size += 1

    def pop_back(self) -> T:
        """Removes and returns the last item in the queue."""
        if self.is_empty():
            raise IndexError("Buffer is empty.")
        self.tail = (self.tail - 1) % self.capacity
        self.size -= 1
        return self.buffer[self.tail]

    def pop_front(self) -> T:
        """Removes and returns the first item in the queue."""
        if self.is_empty():
            raise IndexError("Buffer is empty.")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self) -> T:
        """Returns the first item in the queue."""
        if self.is_empty():
            raise IndexError("Buffer is empty.")
        return self.buffer[self.head]


def test():
    queue = CircularQueue(3)
    queue.push_back(1)
    queue.push_back(2)
    queue.push_back(3)
    queue.push_back(4)
    assert len(queue) == 3

    queue = CircularQueue(3)
    queue.push_back(2)
    queue.push_front(1)
    assert len(queue) == 2
    assert queue.peek() == 1
    assert queue.pop_front() == 1
    assert queue.pop_front() == 2

    queue = CircularQueue(3)
    queue.push_back(1)
    queue.push_back(2)
    queue.push_back(3)
    queue.push_back(4)
    assert queue.pop_back() == 4
    assert queue.pop_back() == 3
    assert queue.pop_back() == 2

    queue = CircularQueue(3)
    queue.push_front(1)
    queue.push_front(2)
    queue.push_front(3)
    queue.push_front(4)
    assert queue.pop_back() == 2
