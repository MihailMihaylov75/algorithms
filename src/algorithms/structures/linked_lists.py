"""
Problem:
Provide minimal linked-list node structures and common operations.

Singly-linked (SinglyNode):
- cycle_check(head): detect a cycle using Floyd's algorithm.
- reverse(head): reverse the list and return the new head.
- nth_to_last(head, n): return the n-th to last node (1-based; n=1 → last).

Doubly-linked (DoublyNode):
- Minimal node data structure for completeness.

Examples:
    # Singly
    a = SinglyNode(1, SinglyNode(2, SinglyNode(3)))
    has_cycle = cycle_check(a)            # False
    new_head = reverse(a)                 # 3 -> 2 -> 1
    node = nth_to_last(new_head, 2)       # value 2

    # Doubly
    d1 = DoublyNode(10)
    d2 = DoublyNode(20, prev_node=d1)
    d1.next = d2

Notes:
- Educational implementations focused on clarity, not utilities.
- All operations are O(n) time, O(1) extra space unless stated otherwise.
"""

from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class SinglyNode(Generic[T]):
    """
    Node for a singly linked list.

    :param value: Payload value.
    :param next: Reference to the next node (or None).
    """

    __slots__ = ("value", "next")

    def __init__(self, value: T, next: SinglyNode[T] | None = None) -> None:
        self.value: T = value
        self.next: SinglyNode[T] | None = next


def cycle_check(head: SinglyNode[T] | None) -> bool:
    """
    Detects whether the given singly linked list contains a cycle.

    :param head: Head node of the list (or None for empty).
    :return: True if a cycle exists, False otherwise.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    slow: SinglyNode[T] | None = head
    fast: SinglyNode[T] | None = head

    while fast is not None and fast.next is not None:
        slow = slow.next if slow is not None else None
        fast = fast.next.next
        if slow is not None and slow is fast:
            return True
    return False


def reverse(head: SinglyNode[T] | None) -> SinglyNode[T] | None:
    """
    Reverses a singly linked list and returns the new head.

    :param head: Head node of the list (or None).
    :return: New head after reversal.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    prev: SinglyNode[T] | None = None
    curr: SinglyNode[T] | None = head

    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def nth_to_last(head: SinglyNode[T] | None, n: int) -> SinglyNode[T]:
    """
    Returns the n-th to last node (1-based). For example, n=1 -> last node.

    :param head: Head node of the list (must be non-empty and long enough).
    :param n: 1-based distance from the tail.
    :return: The n-th to last node.
    :raises ValueError: If n < 1 or list is shorter than n nodes.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    lead: SinglyNode[T] | None = head
    for _ in range(n):
        if lead is None:
            raise ValueError("n is larger than the size of the linked list")
        lead = lead.next

    follow: SinglyNode[T] | None = head
    while lead is not None:
        # both pointers advance until lead hits the end
        follow = follow.next if follow is not None else None
        lead = lead.next

    if follow is None:
        # head was None or list shorter than n (already guarded, but keep for safety)
        raise ValueError("List is empty or shorter than n")

    return follow


class DoublyNode(Generic[T]):
    """
    Node for a doubly linked list.

    :param value: Payload value.
    :param prev_node: Previous node.
    :param next_node: Next node.
    """

    __slots__ = ("value", "prev", "next")

    def __init__(
        self,
        value: T,
        prev_node: DoublyNode[T] | None = None,
        next_node: DoublyNode[T] | None = None,
    ) -> None:
        self.value: T = value
        self.prev: DoublyNode[T] | None = prev_node
        self.next: DoublyNode[T] | None = next_node
