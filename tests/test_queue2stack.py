__author__ = 'Mihail Mihaylov'
import pytest

from src.algorithms.structures.queue2stack import Queue2Stack


def test_enqueue_then_dequeue_returns_first_in(empty_queue2stack: Queue2Stack[int]) -> None:
    empty_queue2stack.enqueue(1)
    empty_queue2stack.enqueue(2)
    assert empty_queue2stack.dequeue() == 1


def test_size_after_multiple_enqueues(empty_queue2stack: Queue2Stack[int]) -> None:
    empty_queue2stack.enqueue(1)
    empty_queue2stack.enqueue(2)
    assert empty_queue2stack.size() == 2


def test_dequeue_returns_in_fifo_order(empty_queue2stack: Queue2Stack[int]) -> None:
    empty_queue2stack.enqueue(1)
    empty_queue2stack.enqueue(2)
    empty_queue2stack.enqueue(3)
    empty_queue2stack.dequeue()  # removes 1
    assert empty_queue2stack.dequeue() == 2


def test_dequeue_on_empty_raises(empty_queue2stack: Queue2Stack[int]) -> None:
    with pytest.raises(IndexError):
        empty_queue2stack.dequeue()


def test_is_empty_on_new_queue2stack(empty_queue2stack: Queue2Stack[int]) -> None:
    assert empty_queue2stack.is_empty()

