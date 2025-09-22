"""
Problem:
Implement a LIFO (last-in, first-out) stack with operations:
push, pop, peek, is_empty, size.

Notes:
- This educational implementation uses a Python list:
  - push(): append at the end          → O(1) amortized
  - pop(): pop from the end            → O(1)
  - peek(): read the last element      → O(1)
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """A simple LIFO stack backed by a Python list."""

    def __init__(self) -> None:
        """Initializes an empty stack."""
        self._items: list[T] = []

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        :return: True if no elements, False otherwise.
        """
        return not self._items

    def push(self, item: T) -> None:
        """
        Pushes an element on top of the stack.

        :param item: Element to push.
        """
        self._items.append(item)

    def pop(self) -> T:
        """
        Removes and returns the top element (LIFO).

        :return: The popped element.
        :raises IndexError: If the stack is empty.
        """
        return self._items.pop()

    def peek(self) -> T:
        """
        Returns (without removing) the top element.

        :return: The top element.
        :raises IndexError: If the stack is empty.
        """
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def size(self) -> int:
        """
        Returns the number of elements in the stack.

        :return: Size of the stack.
        """
        return len(self._items)
