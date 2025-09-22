__author__ = 'Mihail Mihaylov'
import pytest
from src.algorithms.structures.stack import Stack


@pytest.fixture
def empty_stack() -> Stack[int]:
    """Provides a fresh empty stack for each test."""
    return Stack[int]()
