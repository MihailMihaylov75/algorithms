"""
Problem:
Implement a double-ended queue (deque) data structure that supports adding
and removing elements from both the front and the rear.

Examples:
    dq = Deque()
    dq.add_front(10)
    dq.add_rear(20)
    dq.remove_front()  -> 10
    dq.remove_rear()   -> 20
"""

from typing import Generic, List, TypeVar

T = TypeVar("T")


class Deque(Generic[T]):
    """
    A simple double-ended queue (deque) implementation backed by a Python list.

    Supports:
    - Adding to front and rear
    - Removing from front and rear
    - Checking if empty
    - Querying size
    """

    def __init__(self) -> None:
        """Initializes an empty deque."""
        self._items: List[T] = []

    def is_empty(self) -> bool:
        """
        Checks if the deque is empty.

        :return: True if no elements, False otherwise.
        """
        return not self._items

    def add_front(self, item: T) -> None:
        """
        Adds an element to the rear (end) of the deque.

        :param item: Element to add.
        """
        self._items.append(item)

    def add_rear(self, item: T) -> None:
        """
        Adds an element to the front (beginning) of the deque.

        :param item: Element to add.
        """
        self._items.insert(0, item)

    def remove_front(self) -> T:
        """
        Removes and returns the element from the rear (end) of the deque.

        :return: The removed element.
        :raises IndexError: If the deque is empty.
        """
        return self._items.pop()

    def remove_rear(self) -> T:
        """
        Removes and returns the element from the front (beginning) of the deque.

        :return: The removed element.
        :raises IndexError: If the deque is empty.
        """
        return self._items.pop(0)

    def size(self) -> int:
        """
        Returns the number of elements in the deque.

        :return: Size of the deque.
        """
        return len(self._items)
