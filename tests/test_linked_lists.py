__author__ = 'Mihail Mihaylov'
# tests/test_linked_list.py
import pytest

from src.algorithms.structures.linked_lists import SinglyNode, cycle_check, nth_to_last, reverse


def test_cycle_check_detects_cycle() -> None:
    a = SinglyNode(1)
    b = SinglyNode(2)
    c = SinglyNode(3)
    a.next = b
    b.next = c
    c.next = a
    assert cycle_check(a)


def test_reverse_returns_new_head_value() -> None:
    a = SinglyNode(1, SinglyNode(2, SinglyNode(3)))
    new_head = reverse(a)
    assert new_head.value == 3


def test_nth_to_last_returns_correct_value() -> None:
    a = SinglyNode(1, SinglyNode(2, SinglyNode(3)))
    node = nth_to_last(a, 2)
    assert node.value == 2


def test_nth_to_last_raises_when_n_too_large() -> None:
    a = SinglyNode(1, SinglyNode(2))
    with pytest.raises(ValueError):
        nth_to_last(a, 3)
