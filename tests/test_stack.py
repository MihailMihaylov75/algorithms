__author__ = 'Mihail Mihaylov'
import pytest
from src.algorithms.structures.stack import Stack


def test_push_then_pop_returns_last_pushed() -> None:
    st = Stack[int]()
    st.push(1)
    assert st.pop() == 1


def test_peek_returns_top_without_removal() -> None:
    st = Stack[int]()
    st.push(10)
    assert st.peek() == 10


def test_size_after_multiple_pushes() -> None:
    st = Stack[int]()
    st.push(1)
    st.push(2)
    assert st.size() == 2


def test_pop_on_empty_raises() -> None:
    st = Stack[int]()
    with pytest.raises(IndexError):
        st.pop()
