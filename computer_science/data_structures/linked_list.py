from typing import Any, Optional


class SinglyLinkedListNode:
    """Node for singly linked list."""

    def __init__(self, value: Any) -> None:
        """Initializes a node with the given value.

        Args:
            value (Any): The value to store in the node.
        """
        self._value = value
        self._next: Optional[SinglyLinkedListNode] = None


class DoublyLinkedListNode:
    """Node for doubly linked list."""

    def __init__(self, value: Any) -> None:
        """Initializes a node with the given value.

        Args:
            value (Any): The value to store in the node.
        """
        self._value = value
        self._next: Optional[DoublyLinkedListNode] = None
        self._prev: Optional[DoublyLinkedListNode] = None


class SinglyLinkedList:
    """Singly linked list implementation."""

    def __init__(self) -> None:
        """Initializes an empty singly linked list."""
        self._head: Optional[SinglyLinkedListNode] = None

    def insert_at_head(self, value: Any) -> None:
        """Inserts a new node with value at the head.

        Args:
            value (Any): The value to insert.
        """
        node = SinglyLinkedListNode(value=value)
        node._next = self._head
        self._head = node

    def insert_at_tail(self, value: Any) -> None:
        """Inserts a new node with value at the tail.

        Args:
            value (Any): The value to insert.
        """
        node = SinglyLinkedListNode(value=value)
        if not self._head:
            self._head = node
            return
        current = self._head
        while current._next:
            current = current._next
        current._next = node

    def delete(self, value: Any) -> None:
        """Deletes the first occurrence of a node with the given value.

        Args:
            value (Any): The value of the node to delete.
        """
        current = self._head
        prev: Optional[SinglyLinkedListNode] = None
        while current:
            if current._value == value:
                if prev:
                    prev._next = current._next
                else:
                    self._head = current._next
                return
            prev = current
            current = current._next

    def traverse(self) -> None:
        """Prints elements with head and tail labels."""
        if not self._head:
            print("")
            return
        elements = []
        current = self._head
        while current:
            if current == self._head:
                elements.append(f"{current._value} (head)")
            elif current._next is None:
                elements.append(f"{current._value} (tail)")
            else:
                elements.append(str(current._value))
            current = current._next
        print(" -> ".join(elements))


class CircularSinglyLinkedList(SinglyLinkedList):
    """Circular singly linked list with head/tail arrows."""

    def insert_at_tail(self, value: Any) -> None:
        """Inserts a new node with value at the tail of the circular list.

        Args:
            value (Any): The value to insert.
        """
        node = SinglyLinkedListNode(value=value)
        if not self._head:
            self._head = node
            node._next = node
            return
        current = self._head
        while current._next != self._head:
            current = current._next
        current._next = node
        node._next = self._head

    def traverse(self) -> None:
        """Prints elements with head and tail labels, showing circular loop."""
        if not self._head:
            print("")
            return
        elements = []
        current = self._head
        while True:
            if current == self._head:
                elements.append(f"{current._value} (head)")
            elif current._next == self._head:
                elements.append(f"{current._value} (tail)")
            else:
                elements.append(str(current._value))
            current = current._next
            if current == self._head:
                break
        print(" -> ".join(elements) + " -> (head)")


class DoublyLinkedList:
    """Canonical doubly linked list with head/tail arrows."""

    def __init__(self) -> None:
        """Initializes an empty doubly linked list."""
        self._head: Optional[DoublyLinkedListNode] = None

    def insert_at_head(self, value: Any) -> None:
        """Inserts a new node with value at the head.

        Args:
            value (Any): The value to insert.
        """
        node = DoublyLinkedListNode(value=value)
        if self._head:
            node._next = self._head
            self._head._prev = node
        self._head = node

    def insert_at_tail(self, value: Any) -> None:
        """Inserts a new node with value at the tail.

        Args:
            value (Any): The value to insert.
        """
        node = DoublyLinkedListNode(value=value)
        if not self._head:
            self._head = node
            return
        current = self._head
        while current._next:
            current = current._next
        current._next = node
        node._prev = current

    def delete(self, value: Any) -> None:
        """Deletes the first occurrence of a node with the given value.

        Args:
            value (Any): The value of the node to delete.
        """
        current = self._head
        while current:
            if current._value == value:
                if current._prev:
                    current._prev._next = current._next
                else:
                    self._head = current._next
                if current._next:
                    current._next._prev = current._prev
                return
            current = current._next

    def traverse_forward(self) -> None:
        """Prints forward traversal with head and tail labels."""
        if not self._head:
            print("")
            return
        elements = []
        current = self._head
        while current:
            if current == self._head:
                elements.append(f"{current._value} (head)")
            elif current._next is None:
                elements.append(f"{current._value} (tail)")
            else:
                elements.append(str(current._value))
            current = current._next
        print(" <-> ".join(elements))

    def traverse_backward(self) -> None:
        """Prints backward traversal with head and tail labels."""
        if not self._head:
            print("")
            return
        current = self._head
        while current._next:
            current = current._next
        elements = []
        while current:
            if current._next is None:
                elements.append(f"{current._value} (tail)")
            elif current == self._head:
                elements.append(f"{current._value} (head)")
            else:
                elements.append(str(current._value))
            current = current._prev
        print(" <-> ".join(elements))


class CircularDoublyLinkedList(DoublyLinkedList):
    """Circular doubly linked list with head/tail arrows."""

    def insert_at_tail(self, value: Any) -> None:
        """Inserts a new node with value at the tail of the circular doubly linked list.

        Args:
            value (Any): The value to insert.
        """
        node = DoublyLinkedListNode(value=value)
        if not self._head:
            self._head = node
            node._next = node
            node._prev = node
            return
        tail = self._head._prev if self._head._prev else self._head
        tail._next = node
        node._prev = tail
        node._next = self._head
        self._head._prev = node

    def traverse_forward(self) -> None:
        """Prints forward traversal with head/tail labels and circular loop."""
        if not self._head:
            print("")
            return
        elements = []
        current = self._head
        while True:
            if current == self._head:
                elements.append(f"{current._value} (head)")
            elif current._next == self._head:
                elements.append(f"{current._value} (tail)")
            else:
                elements.append(str(current._value))
            current = current._next
            if current == self._head:
                break
        print(" <-> ".join(elements) + " <-> (head)")

    def traverse_backward(self) -> None:
        """Prints backward traversal with head/tail labels and circular loop."""
        if not self._head:
            print("")
            return
        elements = []
        current = self._head._prev if self._head._prev else self._head
        start = current
        while True:
            if current._next == self._head:
                elements.append(f"{current._value} (tail)")
            elif current == self._head:
                elements.append(f"{current._value} (head)")
            else:
                elements.append(str(current._value))
            current = current._prev
            if current == start:
                break
        print(" <-> ".join(elements))


if __name__ == "__main__":
    # Singly Linked List
    print("Singly Linked List Operations:")
    sll = SinglyLinkedList()
    print("Insert 1 at head")
    sll.insert_at_head(value=1)
    print("Insert 2 at tail")
    sll.insert_at_tail(value=2)
    print("Insert 3 at tail")
    sll.insert_at_tail(value=3)
    print("Traverse list:")
    sll.traverse()
    print("Delete 2")
    sll.delete(value=2)
    print("Traverse after deletion:")
    sll.traverse()

    # Circular Singly Linked List
    print("\nCircular Singly Linked List Operations:")
    csll = CircularSinglyLinkedList()
    print("Insert 10 at tail")
    csll.insert_at_tail(value=10)
    print("Insert 20 at tail")
    csll.insert_at_tail(value=20)
    print("Insert 30 at tail")
    csll.insert_at_tail(value=30)
    print("Traverse circular list:")
    csll.traverse()

    # Doubly Linked List
    print("\nDoubly Linked List Operations:")
    dll = DoublyLinkedList()
    print("Insert 5 at head")
    dll.insert_at_head(value=5)
    print("Insert 10 at tail")
    dll.insert_at_tail(value=10)
    print("Insert 15 at tail")
    dll.insert_at_tail(value=15)
    print("Traverse forward:")
    dll.traverse_forward()
    print("Traverse backward:")
    dll.traverse_backward()
    print("Delete 10")
    dll.delete(value=10)
    print("Traverse forward after deletion:")
    dll.traverse_forward()

    # Circular Doubly Linked List
    print("\nCircular Doubly Linked List Operations:")
    cdll = CircularDoublyLinkedList()
    print("Insert 100 at tail")
    cdll.insert_at_tail(value=100)
    print("Insert 200 at tail")
    cdll.insert_at_tail(value=200)
    print("Insert 300 at tail")
    cdll.insert_at_tail(value=300)
    print("Traverse forward:")
    cdll.traverse_forward()
    print("Traverse backward:")
    cdll.traverse_backward()
