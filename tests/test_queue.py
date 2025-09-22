__author__ = 'Mihail Mihaylov'
import pytest

from src.algorithms.structures.queue import Queue


def test_enqueue_then_dequeue_returns_first_in(empty_queue: Queue[int]) -> None:
    empty_queue.enqueue(1)
    assert empty_queue.dequeue() == 1


def test_size_after_two_enqueues(empty_queue: Queue[int]) -> None:
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    assert empty_queue.size() == 2


def test_is_empty_on_new_queue(empty_queue: Queue[int]) -> None:
    assert empty_queue.is_empty()


def test_dequeue_on_empty_raises(empty_queue: Queue[int]) -> None:
    with pytest.raises(IndexError):
        empty_queue.dequeue()
