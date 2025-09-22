__author__ = 'Mihail Mihaylov'
import pytest
from src.algorithms.structures.queue import Queue


def test_enqueue_then_dequeue_returns_first_in() -> None:
    q = Queue[int]()
    q.enqueue(1)
    assert q.dequeue() == 1


def test_size_after_two_enqueues() -> None:
    q = Queue[int]()
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2


def test_is_empty_on_new_queue() -> None:
    q = Queue[int]()
    assert q.is_empty()


def test_dequeue_on_empty_raises() -> None:
    q = Queue[int]()
    with pytest.raises(IndexError):
        q.dequeue()
