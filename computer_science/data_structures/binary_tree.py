from collections import deque
from typing import Any, Optional


class BinaryTreeNode:
    """A node in a binary tree."""

    def __init__(self, data: Any) -> None:
        """Initialize a binary tree node with given data."""
        self.data = data
        self.left: Optional[BinaryTreeNode] = None
        self.right: Optional[BinaryTreeNode] = None

    def __str__(self) -> str:
        """Return a string representation of the node."""
        return str(self.data)


class BinaryTree:
    """A binary tree implementation."""

    def __init__(self) -> None:
        """Initialize an empty binary tree."""
        self.root: Optional[BinaryTreeNode] = None

    def insert(self, data: Any) -> None:
        """Insert a new node with the given data using level-order insertion."""
        if not self.root:
            self.root = BinaryTreeNode(data)
            return

        queue: deque[BinaryTreeNode] = deque([self.root])
        while queue:
            node = queue.popleft()

            if not node.left:
                node.left = BinaryTreeNode(data)
                return
            queue.append(node.left)

            if not node.right:
                node.right = BinaryTreeNode(data)
                return
            queue.append(node.right)

    def inorder_traversal(self) -> list[Any]:
        """Return a list of node values from an inorder traversal."""

        def _inorder(node: Optional[BinaryTreeNode]) -> list[Any]:
            if not node:
                return []
            return _inorder(node.left) + [node.data] + _inorder(node.right)

        return _inorder(self.root)

    def preorder_traversal(self) -> list[Any]:
        """Return a list of node values from a preorder traversal."""

        def _preorder(node: Optional[BinaryTreeNode]) -> list[Any]:
            if not node:
                return []
            return [node.data] + _preorder(node.left) + _preorder(node.right)

        return _preorder(self.root)

    def postorder_traversal(self) -> list[Any]:
        """Return a list of node values from a postorder traversal."""

        def _postorder(node: Optional[BinaryTreeNode]) -> list[Any]:
            if not node:
                return []
            return _postorder(node.left) + _postorder(node.right) + [node.data]

        return _postorder(self.root)

    def level_order_traversal(self) -> list[Any]:
        """Return a list of node values from a level-order traversal."""
        if not self.root:
            return []

        result: list[Any] = []
        queue: deque[BinaryTreeNode] = deque([self.root])

        while queue:
            node = queue.popleft()
            result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def height(self) -> int:
        """Return the height of the tree."""

        def _height(node: Optional[BinaryTreeNode]) -> int:
            if not node:
                return -1
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    def __str__(self) -> str:
        """Return a string representation of the tree using level-order traversal."""
        return str(self.level_order_traversal())
