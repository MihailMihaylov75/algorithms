"""
Problem:
Implement a simple binary tree with node references and basic operations:
- insert_left / insert_right with "push-down" semantics (if a child exists,
  the new node becomes the child and the old one is pushed down one level).
- inorder traversal for verification.

Examples:
    root = BTNode(10)
    root.insert_left(5)           # 5 becomes the left child
    root.insert_right(15)         # 15 becomes the right child
    root.left.insert_right(7)     # push-down if a child already exists
    inorder(root)  -> [5, 7, 10, 15]

Notes:
- Nodes are generic (BTNode[T]).
- insert_* are O(1); traversal is O(n).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


@dataclass
class BTNode(Generic[T]):
    """
    Binary tree node with optional left/right children.

    Attributes:
        value: Value stored in this node.
        left: Left child (or None).
        right: Right child (or None).
    """
    value: T
    left: Optional["BTNode[T]"] = None
    right: Optional["BTNode[T]"] = None

    def insert_left(self, value: T) -> None:
        """
        Insert a new node on the left. If a left child already exists,
        push it down by making it the left child of the newly inserted node.

        Time Complexity: O(1)
        """
        if self.left is None:
            self.left = BTNode(value)
        else:
            self.left = BTNode(value, left=self.left)

    def insert_right(self, value: T) -> None:
        """
        Insert a new node on the right. If a right child already exists,
        push it down by making it the right child of the newly inserted node.

        Time Complexity: O(1)
        """
        if self.right is None:
            self.right = BTNode(value)
        else:
            self.right = BTNode(value, right=self.right)


def inorder(root: Optional[BTNode[T]]) -> List[T]:
    """
    Return the inorder traversal of the tree (left, root, right).

    :param root: Tree root (or None).
    :return: List of values in inorder order.

    Time Complexity: O(n)
    Space Complexity: O(h) recursion stack, where h is tree height.
    """
    if root is None:
        return []
    out: List[T] = []
    out.extend(inorder(root.left))
    out.append(root.value)
    out.extend(inorder(root.right))
    return out
