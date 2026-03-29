class Stack:
    def __init__(self):
        self._data = []
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, x):
        self._data.append(x)
        self._size += 1
        return x

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        x = self._data.pop()
        self._size -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        return self._data[-1]


s = Stack()
s.push(3)
s.push(2)
s.push(1)
print(s.peek())
s.pop()
print(s.peek())
