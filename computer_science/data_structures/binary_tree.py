from collections import deque
from typing import Any, Optional


class BinaryTreeNode:
    """Node class for a binary tree structure."""

    def __init__(self, data: Any) -> None:
        """Initializes a binary tree node with given data.

        Args:
            data (Any): The value to store in the node.
        """
        self._data = data
        self._left: Optional[BinaryTreeNode] = None
        self._right: Optional[BinaryTreeNode] = None

    def __str__(self) -> str:
        """Returns a string representation of the node.

        Returns:
            str: The string representation of the node's data.
        """
        return str(self._data)


class BinaryTree:
    """Binary tree implementation with standard traversal operations."""

    def __init__(self) -> None:
        """Initializes an empty binary tree."""
        self.root: Optional[BinaryTreeNode] = None

    def insert(self, data: Any) -> None:
        """Insert a new node with the given data using level-order insertion."""
        if not self.root:
            self.root = BinaryTreeNode(data)
            return

        queue: deque[BinaryTreeNode] = deque([self.root])
        while queue:
            node = queue.popleft()

            if not node._left:
                node._left = BinaryTreeNode(data)
                return
            queue.append(node._left)

            if not node._right:
                node._right = BinaryTreeNode(data)
                return
            queue.append(node._right)

    def inorder_traversal(self) -> list[Any]:
        """Return a list of node values from an inorder traversal."""

        def _inorder(node: Optional[BinaryTreeNode]) -> list[Any]:
            if not node:
                return []
            return _inorder(node._left) + [node._data] + _inorder(node._right)

        return _inorder(self.root)

    def preorder_traversal(self) -> list[Any]:
        """Return a list of node values from a preorder traversal."""

        def _preorder(node: Optional[BinaryTreeNode]) -> list[Any]:
            if not node:
                return []
            return [node._data] + _preorder(node._left) + _preorder(node._right)

        return _preorder(self.root)

    def postorder_traversal(self) -> list[Any]:
        """Return a list of node values from a postorder traversal."""

        def _postorder(node: Optional[BinaryTreeNode]) -> list[Any]:
            if not node:
                return []
            return _postorder(node._left) + _postorder(node._right) + [node._data]

        return _postorder(self.root)

    def level_order_traversal(self) -> list[Any]:
        """Return a list of node values from a level-order traversal."""
        if not self.root:
            return []

        result: list[Any] = []
        queue: deque[BinaryTreeNode] = deque([self.root])

        while queue:
            node = queue.popleft()
            result.append(node._data)

            if node._left:
                queue.append(node._left)
            if node._right:
                queue.append(node._right)

        return result

    def height(self) -> int:
        """Return the height of the tree."""

        def _height(node: Optional[BinaryTreeNode]) -> int:
            if not node:
                return -1
            return 1 + max(_height(node._left), _height(node._right))

        return _height(self.root)

    def __str__(self) -> str:
        """Return a string representation of the tree using level-order traversal."""
        return str(self.level_order_traversal())


if __name__ == "__main__":
    # Create a binary tree and test its operations
    tree = BinaryTree()

    # Insert some values
    values = [1, 2, 3, 4, 5, 6, 7]
    print("Inserting values:", values)
    for value in values:
        tree.insert(value)

    # Test different traversals
    print("\nTree Traversals:")
    print(f"Inorder:      {tree.inorder_traversal()}")
    print(f"Preorder:     {tree.preorder_traversal()}")
    print(f"Postorder:    {tree.postorder_traversal()}")
    print(f"Level-order:  {tree.level_order_traversal()}")

    # Test other properties
    print(f"\nTree height: {tree.height()}")
    print(f"Tree representation: {tree}")
