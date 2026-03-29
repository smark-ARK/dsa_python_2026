class CircularLinkedList:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        if self.is_empty():
            return "Empty"
        curr = self.tail.next
        res = ""
        while True:
            res += str(curr.value) + "->"
            if curr == self.tail:
                break
            curr = curr.next
        return res

    def insert_first(self, x):
        new_node = self.Node(x)
        if self.is_empty():
            self.tail = new_node
            new_node.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
        self.size += 1
        return x

    def insert_last(self, x):
        new_node = self.Node(x)
        if self.is_empty():
            self.tail = new_node
            new_node.next = self.tail

        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        return x

    def remove_first(self):
        if self.is_empty():
            raise IndexError("List already empty!")
        if self.size == 1:
            self.tail = None
        else:
            x = self.tail.next.value
            self.tail.next = self.tail.next.next
        self.size -= 1
        return x

    def remove_last(self):
        if self.is_empty():
            raise IndexError("List already empty!")
        if self.size == 1:
            self.tail = None
        else:
            # ab kon traverse karinge baap
            pass


cl = CircularLinkedList()

# n1 = cl.Node(1)
# n2 = cl.Node(2)
# n3 = cl.Node(3)

# n1.next = n2
# n2.next = n3
# n3.next = n1
# cl.tail = n3

cl.insert_first(3)
cl.insert_first(2)
cl.insert_first(1)
cl.insert_last(1)
cl.insert_last(2)
cl.insert_last(3)

print(cl)
