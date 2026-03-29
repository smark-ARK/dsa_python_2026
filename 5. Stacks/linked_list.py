class Stack:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        new_node = self.Node(x)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return x

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        x = self.head.value
        if self.size == 1:
            self.head = None
        else:
            self.head = self.head.next
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        return self.head.value


s = Stack()
s.push(3)
s.push(2)
s.push(1)
print(s.peek())
s.pop()
print(s.peek())
