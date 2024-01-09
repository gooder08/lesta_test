class CircularBufferList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.capacity

    def enqueue(self, item):
        if self.is_full():
            self.buffer.pop(0)
        self.buffer.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.buffer.pop(0)

