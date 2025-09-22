__author__ = 'Mihail Mihaylov'
import pytest
from src.algorithms.structures.deque import Deque


def test_add_and_remove_front() -> None:
    dq = Deque[int]()
    dq.add_front(1)
    assert dq.remove_front() == 1


def test_add_and_remove_rear() -> None:
    dq = Deque[int]()
    dq.add_rear(2)
    assert dq.remove_rear() == 2


def test_size_increases_and_decreases() -> None:
    dq = Deque[int]()
    dq.add_front(1)
    dq.add_rear(2)
    assert dq.size() == 2


def test_remove_from_empty_raises() -> None:
    dq = Deque[int]()
    with pytest.raises(IndexError):
        dq.remove_front()

