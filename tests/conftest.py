__author__ = 'Mihail Mihaylov'
import pytest

from src.algorithms.structures.deque import Deque
from src.algorithms.structures.queue import Queue
from src.algorithms.structures.queue2stack import Queue2Stack
from src.algorithms.structures.stack import Stack


@pytest.fixture
def empty_stack() -> Stack[int]:
    """Provides a fresh empty stack for each test."""
    return Stack[int]()


@pytest.fixture
def empty_queue() -> Queue[int]:
    """Provides a fresh empty queue for each test."""
    return Queue[int]()


@pytest.fixture
def empty_deque() -> Deque[int]:
    """Provides a fresh empty deque for each test."""
    return Deque[int]()


@pytest.fixture
def empty_queue2stack() -> Queue2Stack[int]:
    """Provides a fresh empty Queue2Stack for each test."""
    return Queue2Stack[int]()
