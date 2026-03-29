class DoublyLinkedList:
    class Node:
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        curr = self.head
        res = ""
        while curr:
            res += str(curr.value) + "->"
            curr = curr.next
        return res

    def insert_first(self, x):
        new_node = self.Node(x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return x

    def insert_last(self, x):
        new_node = self.Node(x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        return x

    def remove_first(self):
        if self.is_empty():
            raise Exception("List is already empty!")
        x = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return x

    def remove_last(self):
        if self.is_empty():
            raise Exception("List is already empty!")
        x = self.tail.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return x

    def insert(self, x, pos):
        if pos < 0 or pos > self.size + 1:
            raise Exception("Invalid Position!")
        if pos == 1:
            return self.insert_first(x)
        elif pos == self.size + 1:
            return self.insert_last(x)
        else:
            new_node = self.Node(x)
            curr = self.head
            count = 1
            while count != pos - 1:
                curr = curr.next
                count += 1
            succ = curr.next
            new_node.prev = curr
            curr.next = new_node
            new_node.next = succ
            succ.prev = new_node
            self.size += 1
            return x

    def remove(self, pos):
        if pos < 0 or pos > self.size:
            raise Exception("Invalid Position!")
        elif pos == 1:
            return self.remove_first()
        elif pos == self.size:
            return self.remove_last()
        else:
            curr = self.head
            count = 1
            while count != pos:
                curr = curr.next
                count += 1
            x = curr.value
            pred = curr.prev
            succ = curr.next
            pred.next = succ
            succ.prev = pred
            curr.next = curr.prev = None
            self.size -= 1
            return x


dl = DoublyLinkedList()

dl.insert_first(3)
dl.insert_first(2)
dl.insert_first(1)
dl.insert_last(1)
dl.insert_last(2)
dl.insert_last(3)
# n1 = dl.Node(1)
# n2 = dl.Node(2)
# n3 = dl.Node(3)
dl.insert(0, 4)
print("size: ", dl.size)
print(dl)
dl.remove(4)
# n1.next = n2
# n2.next = n3
# n3.next = None
# dl.head = n1
# dl.tail = n3
# dl.size = 3

print("size: ", dl.size)
print(dl)

dl.remove_first()
dl.remove_last()
print("size: ", dl.size)
print(dl)
