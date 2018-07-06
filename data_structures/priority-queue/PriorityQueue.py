import sys
sys.path.append("../heap")
from Heap import Heap

class PriorityQueue(Heap):
    def __init__(self):
        self.heap = [-1] * 10
        self.size = 0
        self.priorities = {}

    def adjust_capacity(self):
        if self.size == len(self.heap):
            heap.append([-1] * (2*size))

    def swap(self, idx1, idx2):
        tmp = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = tmp

    def right_idx(self, idx):
        return idx*2+2

    def left_idx(self, idx):
        return idx*2+1

    def parent_idx(self, idx):
        return (idx-1) // 2

    def right(self, idx):
        return self.heap[self.right_idx(idx)]

    def left(self, idx):
        return self.heap[self.left_idx(idx)]

    def parent(self, idx):
        return self.heap[self.parent_idx(idx)]

    def has_right(self, idx):
        return self.right_idx(idx) < self.size

    def has_left(self, idx):
        return self.left_idx(idx) < self.size

    def has_parent(self, idx):
        return self.parent_idx(idx) >= 0

    def peek(self):
        if self.size == 0:
            raise ValueError()
        return self.heap[0]

    def poll(self):
        if self.size == 0:
            raise ValueError()

        item = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        del self.priorities[item]
        self.heap[self.size] = -1
        self.heapify_down()
        return item

    def add(self, item, priority):
        self.adjust_capacity()
        self.heap[self.size] = item
        self.priorities[item] = priority
        self.size += 1
        self.heapify_up()

    def heapify_down(self):
        idx = 0
        while self.has_left(idx):
            smaller = self.left_idx(idx)
            if self.has_right(idx) and self.priorities[self.right(idx)] < self.priorities[self.left(idx)]:
                smaller = self.right_idx(idx)

            if self.priorities[self.heap[idx]] < self.priorities[self.heap[smaller]]:
                return

            self.swap(idx, smaller)
            idx = smaller

    def heapify_up(self):
        idx = self.size - 1
        while self.has_parent(idx) and self.priorities[self.parent(idx)] > self.priorities[self.heap[idx]]:
            self.swap(idx, self.parent_idx(idx))
            idx = self.parent_idx(idx)
