from collections import deque


class Queue:
    data = deque()
    size = 0

    def enqueue(self, val):
        self.size += 1
        self.data.append(val)

    def dequeue(self):
        self.size -= 1
        return self.data.popleft()

    def empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.data)
