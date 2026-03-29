class Queue:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def len(self):
        return self.size

    def enqueue(self, x):
        new_node = self.Node(x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return x

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Empty!")
        else:
            x = self.head.value
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.size -= 1
            return x

    def first(self):
        if self.is_empty():
            raise IndexError("Queue is Empty!")
        return self.head.value


q = Queue()
print("empty", q.is_empty(), "size", q.len())
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
print("first", q.first(), "size", q.len())  # 3
print("dequeue", q.dequeue(), "size", q.len())  # 3 removed
print("first", q.first(), "size", q.len())  # 2
q.enqueue(10)
print("after enqueue(10): first", q.first(), "size", q.len())  # 2
print("dequeue", q.dequeue())  # 2
print("dequeue", q.dequeue())  # 1
print("dequeue", q.dequeue())  # 10
print("empty", q.is_empty(), "size", q.len())
try:
    q.dequeue()
except Exception as e:
    print("dequeue error", type(e).__name__, e)
