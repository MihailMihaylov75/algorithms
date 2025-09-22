import pytest

from src.algorithms.structures.stack import Stack


def test_push_then_pop_returns_last_pushed(empty_stack: Stack[int]) -> None:
    empty_stack.push(1)
    assert empty_stack.pop() == 1


def test_peek_returns_top_without_removal(empty_stack: Stack[int]) -> None:
    empty_stack.push(10)
    assert empty_stack.peek() == 10


def test_size_after_multiple_pushes(empty_stack: Stack[int]) -> None:
    empty_stack.push(1)
    empty_stack.push(2)
    assert empty_stack.size() == 2


def test_pop_on_empty_raises(empty_stack: Stack[int]) -> None:
    with pytest.raises(IndexError):
        empty_stack.pop()

