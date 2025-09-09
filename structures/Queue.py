from .Node import Node


class Queue:
    def __init__(self, top = None):
        self.top = top

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
        else:
            aux = self.top
            while aux.next is not None:
                aux = aux.next
            aux.next = Node(value)

    def peek(self):
        if not self.isEmpty():
            return self.top.value
        return None

    def pull(self):
        if not self.isEmpty():
            value = self.top.value
            self.top = self.top.next
            return value
        return None

    def isEmpty(self):
        return self.top is None
