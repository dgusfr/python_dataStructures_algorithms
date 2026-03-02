from node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        """Inserts an element at the end of the queue."""
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size += 1

    def pop(self):
        """Removes and returns the element from the front of the queue."""
        if self._size > 0 and self.first is not None:
            elem = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self._size -= 1
            return elem
        raise IndexError("The queue is empty")

    def peek(self):
        """Returns the front element without removing it."""
        if self._size > 0 and self.first is not None:
            elem = self.first.data
            return elem
        raise IndexError("The queue is empty")

    def __len__(self):
        """Returns the current size of the queue."""
        return self._size

    def __repr__(self):
        if self._size > 0:
            result = ""
            current_node = self.first
            while current_node:
                result += str(current_node.data) + " "
                current_node = current_node.next
            return result
        return "Empty Queue"

    def __str__(self):
        return self.__repr__()
