"""
Problem:
Implement a FIFO (first-in, first-out) queue with basic operations:
enqueue, dequeue, is_empty, and size.

Notes:
- This educational implementation uses a Python list:
  - enqueue() inserts at the front (index 0) → O(n)
  - dequeue() pops from the rear (end)       → O(1)
- For production, prefer collections.deque for amortized O(1) on both ends.
"""
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    """
    A simple FIFO queue backed by a Python list.

    Operations:
    - enqueue(x): add element to the front
    - dequeue(): remove element from the rear
    - is_empty(): check if the queue has no elements
    - size(): number of elements in the queue
    """

    def __init__(self) -> None:
        """Initializes an empty queue."""
        self._items: list[T] = []

    def enqueue(self, item: T) -> None:
        """
        Inserts an element at the front (index 0).

        :param item: Element to insert.
        Time Complexity: O(n) due to list insertion at index 0.
        """
        self._items.insert(0, item)

    def dequeue(self) -> T:
        """
        Removes and returns the element from the rear (end).

        :return: The dequeued element.
        :raises IndexError: If the queue is empty.
        Time Complexity: O(1).
        """
        return self._items.pop()

    def is_empty(self) -> bool:
        """
        Checks whether the queue is empty.

        :return: True if empty, False otherwise.
        """
        return not self._items

    def size(self) -> int:
        """
        Returns the number of elements in the queue.

        :return: Size of the queue.
        """
        return len(self._items)
