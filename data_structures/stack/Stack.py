from Node import Node


class Stack:
    def __init__(self):
        self.top = None

    def empty(self):
        return self.top is None

    def peek(self):
        return self.top.data if self.top else -1

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data
