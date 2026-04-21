"""Ex08: Linked List Utility Functions!"""
from __future__ import annotations


class Node:
    """Node in a singly-linked list recursive structure."""
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initialize a Node instance."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Return str rep of the linked list."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


courses: Node = Node(110, Node(210, Node(211, None)))
print(courses)


def value_at(head: Node | None, index: int) -> int:
    """Return the value of the Node or raise an IndexError."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Max value in linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    max_of_rest: int = max(head.next)
    if head.value > max_of_rest:
        return head.value
    return max_of_rest


def linkify(items: list[int]) -> Node | None:
    """Build a linked list from a Python list."""
    if len(items) == 0:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Builds new linked list with values scaled by a factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))
