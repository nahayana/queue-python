class Queue:

    def __init__(self, max_size=None):
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("A fila está cheia.")

        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")

        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")

        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.max_size is None:
            return False

        return len(self.items) >= self.max_size

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()
