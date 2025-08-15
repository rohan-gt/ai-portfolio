from collections.abc import Iterator
from typing import Any, Optional, cast


class SLLNode:
    """Represents a node in a singly linked list."""

    def __init__(self, data: Any) -> None:
        """Initializes a node with data and sets the next node to None."""
        self.data = data
        self.next: Optional["SLLNode"] = None

    def __repr__(self) -> str:
        """Returns a string representation of the node."""
        return f"SLLNode({self.data})"


class DLLNode:
    """Represents a node in a doubly linked list."""

    def __init__(self, data: Any) -> None:
        """Initializes a node with data and sets the next and previous nodes to None."""
        self.data = data
        self.next: Optional["DLLNode"] = None
        self.prev: Optional["DLLNode"] = None

    def __repr__(self) -> str:
        """Returns a string representation of the node."""
        return f"DLLNode({self.data})"


class SinglyLinkedList:
    """A singly linked list implementation."""

    def __init__(self) -> None:
        """Initializes an empty singly linked list."""
        self.head: Optional[SLLNode] = None

    def append(self, data: Any) -> None:
        """Appends a new node with the given data to the end of the list.

        Args:
            data: The data to be added to the list.
        """
        new_node = SLLNode(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __iter__(self) -> Iterator[Any]:
        """Iterates over the nodes in the linked list.

        Yields:
            The data of each node in the list.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self) -> str:
        """Returns a string representation of the linked list.

        Returns:
            str: A string representing the linked list.
        """
        nodes = [str(node) for node in self]
        return " -> ".join(nodes)


class CircularLinkedList:
    """A circular singly linked list implementation."""

    def __init__(self) -> None:
        """Initializes an empty circular linked list."""
        self.head: Optional[SLLNode] = None

    def append(self, data: Any) -> None:
        """Appends a new node with the given data to the end of the list.

        Args:
            data: The data to be added to the list.
        """
        new_node = SLLNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node  # Point to itself for circular
            return

        # At this point we know self.head is not None
        head = cast(SLLNode, self.head)
        current: SLLNode = head
        while current.next != head:
            current = cast(SLLNode, current.next)
        current.next = new_node
        new_node.next = head

    def __iter__(self) -> Iterator[Any]:
        """Iterates over the nodes in the circular linked list.

        Yields:
            The data of each node in the list.
        """
        if not self.head:
            return
        head = cast(SLLNode, self.head)
        current: SLLNode = head
        yield current.data
        current = cast(SLLNode, current.next)
        while current != head:
            yield current.data
            current = cast(SLLNode, current.next)

    def __repr__(self) -> str:
        """Returns a string representation of the circular linked list.

        Returns:
            str: A string representing the circular linked list.
        """
        nodes = [str(node) for node in self]
        if not nodes:
            return ""
        if len(nodes) == 1:
            return nodes[0]
        return " -> ".join(nodes) + " -> (head)"


class DoublyLinkedList:
    """A doubly linked list implementation."""

    def __init__(self) -> None:
        """Initializes an empty doubly linked list."""
        self.head: Optional[DLLNode] = None

    def append(self, data: Any) -> None:
        """Appends a new node with the given data to the end of the list.

        Args:
            data: The data to be added to the list.
        """
        new_node = DLLNode(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def __iter__(self) -> Iterator[Any]:
        """Iterates over the nodes in the linked list.

        Yields:
            The data of each node in the list.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next
        # Note: This iteration goes forward only.

    def __repr__(self) -> str:
        """Returns a string representation of the linked list.

        Returns:
            str: A string representing the linked list.
        """
        nodes = [str(node) for node in self]
        return " <-> ".join(nodes)


class DoublyCircularLinkedList:
    """A circular doubly linked list implementation."""

    def __init__(self) -> None:
        """Initializes an empty circular doubly linked list."""
        self.head: Optional[DLLNode] = None

    def append(self, data: Any) -> None:
        """Appends a new node with the given data to the end of the list.

        Args:
            data: The data to be added to the list.
        """
        new_node = DLLNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        # At this point we know self.head is not None
        head = cast(DLLNode, self.head)
        last = cast(DLLNode, head.prev)
        last.next = new_node
        new_node.prev = last
        new_node.next = head
        head.prev = new_node

    def __iter__(self) -> Iterator[Any]:
        """Iterates over the nodes in the circular doubly linked list.

        Yields:
            The data of each node in the list.
        """
        if not self.head:
            return
        head = cast(DLLNode, self.head)
        current: DLLNode = head
        yield current.data
        current = cast(DLLNode, current.next)
        while current != head:
            yield current.data
            current = cast(DLLNode, current.next)

    def __repr__(self) -> str:
        """Returns a string representation of the circular doubly linked list.

        Returns:
            str: A string representing the circular doubly linked list.
        """
        nodes = [str(node) for node in self]
        if not nodes:
            return ""
        if len(nodes) == 1:
            return nodes[0]
        return " <-> ".join(nodes) + " <-> (head)"
