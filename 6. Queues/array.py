class Queue:
    def __init__(self):
        self._data = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def len(self):
        return self.size

    def enqueue(self, x):
        self._data.append(x)
        self.size += 1
        return x

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Empty!")

        x = self._data.pop(0)
        self.size -= 1
        return x

    def first(self):
        if self.is_empty():
            raise IndexError("Queue is Empty!")
        return self._data[0]


q = Queue()
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
print(q.first())
q.dequeue()
print(q.first())
