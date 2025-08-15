from typing import Any, Optional


class BSTNode:
    """A node in a binary search tree."""

    def __init__(self, data: Any) -> None:
        """Initialize a BST node with given data."""
        self.data = data
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

    def __str__(self) -> str:
        """Return a string representation of the node."""
        return str(self.data)


class BinarySearchTree:
    """A binary search tree implementation."""

    def __init__(self) -> None:
        """Initialize an empty binary search tree."""
        self.root: Optional[BSTNode] = None

    def insert(self, data: Any) -> None:
        """Insert a new node with the given data."""
        if not self.root:
            self.root = BSTNode(data)
            return

        def _insert(node: BSTNode, data: Any) -> None:
            if data < node.data:
                if node.left is None:
                    node.left = BSTNode(data)
                else:
                    _insert(node.left, data)
            else:
                if node.right is None:
                    node.right = BSTNode(data)
                else:
                    _insert(node.right, data)

        _insert(self.root, data)

    def search(self, data: Any) -> bool:
        """Search for a value in the BST."""

        def _search(node: Optional[BSTNode], data: Any) -> bool:
            if not node:
                return False
            if node.data == data:
                return True
            if data < node.data:
                return _search(node.left, data)
            return _search(node.right, data)

        return _search(self.root, data)

    def delete(self, data: Any) -> None:
        """Delete a node with the given data from the BST."""

        def _min_value_node(node: BSTNode) -> BSTNode:
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node: Optional[BSTNode], data: Any) -> Optional[BSTNode]:
            if not node:
                return None

            if data < node.data:
                node.left = _delete(node.left, data)
            elif data > node.data:
                node.right = _delete(node.right, data)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                temp = _min_value_node(node.right)
                node.data = temp.data
                node.right = _delete(node.right, temp.data)

            return node

        self.root = _delete(self.root, data)

    def inorder_traversal(self) -> list[Any]:
        """Return a list of node values from an inorder traversal."""

        def _inorder(node: Optional[BSTNode]) -> list[Any]:
            if not node:
                return []
            return _inorder(node.left) + [node.data] + _inorder(node.right)

        return _inorder(self.root)

    def __str__(self) -> str:
        """Return a string representation of the BST using inorder traversal."""
        return str(self.inorder_traversal())
