from Node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def peek(self):
        return self.head.data if self.head else -1

    def add(self, data):
        node = Node(data)

        if self.tail:
            self.tail.next = node
        self.tail = node

        if not self.head:
            self.head = node

    def pop(self):
        data = self.head.data
        self.head = self.head.next

        if not self.head:
            self.tail = None
        return data
