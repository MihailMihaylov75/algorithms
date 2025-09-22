__author__ = 'Mihail Mihaylov'
"""
Problem:
Implement a FIFO queue using two stacks (lists).
- enqueue(x): push element to instack.
- dequeue(): if outstack is empty, move all from instack → outstack, then pop.

Example:
    q = Queue2Stack[int]()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()  -> 1
    q.dequeue()  -> 2

Complexities:
- Enqueue: O(1).
- Dequeue: Amortized O(1), worst-case O(n) when transferring.
"""

from typing import Generic, List, TypeVar

T = TypeVar("T")


class Queue2Stack(Generic[T]):
    """A queue implemented using two stacks."""

    def __init__(self) -> None:
        """Initializes empty instack and outstack."""
        self._instack: List[T] = []
        self._outstack: List[T] = []

    def enqueue(self, element: T) -> None:
        """
        Adds an element to the queue.

        :param element: Element to enqueue.
        Time Complexity: O(1).
        """
        self._instack.append(element)

    def dequeue(self) -> T:
        """
        Removes and returns the first enqueued element (FIFO).

        :return: The dequeued element.
        :raises IndexError: If the queue is empty.
        Time Complexity: Amortized O(1).
        """
        if not self._outstack:
            while self._instack:
                self._outstack.append(self._instack.pop())
        return self._outstack.pop()

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        :return: True if empty, False otherwise.
        """
        return not self._instack and not self._outstack

    def size(self) -> int:
        """
        Returns the number of elements in the queue.

        :return: Size of the queue.
        """
        return len(self._instack) + len(self._outstack)
