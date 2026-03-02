from typing import Optional
from node import Node


class Stack:
    def __init__(self):
        self.top: Optional[Node] = None
        self._size = 0

    def push(self, elem):
        """Inserts an element into the stack."""
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        """Removes the element from the top of the stack and returns it."""
        if self.top is not None:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data

        raise IndexError("The stack is empty")

    def peek(self):
        """Returns the top element without removing it."""
        if self.top is not None:
            return self.top.data

        raise IndexError("The stack is empty")

    def __len__(self):
        """Returns the size of the stack."""
        return self._size

    def __repr__(self):
        result = ""
        current_node = self.top

        while current_node is not None:
            result += str(current_node.data) + "\n"
            current_node = current_node.next

        return result

    def __str__(self):
        return self.__repr__()
