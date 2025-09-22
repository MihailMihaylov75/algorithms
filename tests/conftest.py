__author__ = 'Mihail Mihaylov'
import pytest
from src.algorithms.structures.stack import Stack
from src.algorithms.structures.queue import Queue


@pytest.fixture
def empty_stack() -> Stack[int]:
    """Provides a fresh empty stack for each test."""
    return Stack[int]()


@pytest.fixture
def empty_queue() -> Queue[int]:
    """Provides a fresh empty queue for each test."""
    return Queue[int]()
