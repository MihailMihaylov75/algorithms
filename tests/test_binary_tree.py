__author__ = 'Mihail Mihaylov'
from src.algorithms.structures.binary_tree import BTNode, inorder


def test_insert_left_creates_child() -> None:
    root = BTNode(3)
    root.insert_left(4)
    assert root.left.value == 4  # type: ignore[union-attr]


def test_insert_left_pushes_existing_down() -> None:
    root = BTNode(10)
    root.insert_left(1)
    root.insert_left(2)
    assert (root.left.value, root.left.left.value) == (2, 1)  # type: ignore[union-attr]


def test_insert_right_pushes_existing_down() -> None:
    root = BTNode(10)
    root.insert_right(20)
    root.insert_right(30)
    assert (root.right.value, root.right.right.value) == (30, 20)  # type: ignore[union-attr]


def test_inorder_traversal() -> None:
    root = BTNode(10)
    root.insert_left(5)
    root.left.insert_right(7)  # type: ignore[union-attr]
    root.insert_right(15)
    assert inorder(root) == [5, 7, 10, 15]
