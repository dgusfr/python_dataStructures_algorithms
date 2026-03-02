from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional["Node"] = None
