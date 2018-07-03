from Node import Node


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            tmp = Node(data)
            tmp.next = self.head
            self.head = tmp

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next

