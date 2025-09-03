from typing import Any, Optional


class BinarySearchTreeNode:
    """Node class for a binary search tree structure."""

    def __init__(self, data: Any) -> None:
        """Initializes a BST node with given data.

        Args:
            data (Any): The value to store in the node.
        """
        self._data = data
        self._left: Optional[BinarySearchTreeNode] = None
        self._right: Optional[BinarySearchTreeNode] = None

    def __str__(self) -> str:
        """Returns a string representation of the node.

        Returns:
            str: The string representation of the node's data.
        """
        return str(self._data)


class BinarySearchTree:
    """Binary search tree implementation with O(log n) operations."""

    def __init__(self) -> None:
        """Initialize an empty binary search tree."""
        self.root: Optional[BinarySearchTreeNode] = None

    def insert(self, data: Any) -> None:
        """Insert a new node with the given data."""
        if not self.root:
            self.root = BinarySearchTreeNode(data)
            return

        def _insert(node: BinarySearchTreeNode, data: Any) -> None:
            if data < node._data:
                if node._left is None:
                    node._left = BinarySearchTreeNode(data)
                else:
                    _insert(node._left, data)
            else:
                if node._right is None:
                    node._right = BinarySearchTreeNode(data)
                else:
                    _insert(node._right, data)

        _insert(self.root, data)

    def search(self, data: Any) -> bool:
        """Search for a value in the BST."""

        def _search(node: Optional[BinarySearchTreeNode], data: Any) -> bool:
            if not node:
                return False
            if node._data == data:
                return True
            if data < node._data:
                return _search(node._left, data)
            return _search(node._right, data)

        return _search(self.root, data)

    def delete(self, data: Any) -> None:
        """Delete a node with the given data from the BST."""

        def _min_value_node(node: BinarySearchTreeNode) -> BinarySearchTreeNode:
            current = node
            while current._left:
                current = current._left
            return current

        def _delete(node: Optional[BinarySearchTreeNode], data: Any) -> Optional[BinarySearchTreeNode]:
            if not node:
                return None

            if data < node._data:
                node._left = _delete(node._left, data)
            elif data > node._data:
                node._right = _delete(node._right, data)
            else:
                if not node._left:
                    return node._right
                elif not node._right:
                    return node._left

                temp = _min_value_node(node._right)
                node._data = temp._data
                node._right = _delete(node._right, temp._data)

            return node

        self.root = _delete(self.root, data)

    def inorder_traversal(self) -> list[Any]:
        """Return a list of node values from an inorder traversal."""

        def _inorder(node: Optional[BinarySearchTreeNode]) -> list[Any]:
            if not node:
                return []
            return _inorder(node._left) + [node._data] + _inorder(node._right)

        return _inorder(self.root)

    def __str__(self) -> str:
        """Return a string representation of the BST using inorder traversal."""
        return str(self.inorder_traversal())


if __name__ == "__main__":
    # Create a binary search tree and test its operations
    bst = BinarySearchTree()

    # Insert some values
    values = [50, 30, 70, 20, 40, 60, 80]
    print("Inserting values:", values)
    for value in values:
        bst.insert(value)
    print(f"BST after insertions (inorder): {bst}")

    # Test search operations
    print("\nSearch operations:")
    search_values = [40, 90]  # One exists, one doesn't
    for value in search_values:
        result = "found" if bst.search(value) else "not found"
        print(f"Value {value} is {result}")

    # Test deletion
    print("\nDeletion operations:")
    delete_values = [30, 70]  # Delete a node with one child and a node with two children
    for value in delete_values:
        print(f"Deleting {value}")
        bst.delete(value)
        print(f"BST after deletion (inorder): {bst}")
