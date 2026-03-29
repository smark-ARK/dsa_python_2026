class SinglyLinkedList:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        curr = self.head
        res = ""
        while curr:
            res += str(curr.value) + " -> "
            curr = curr.next
        return res + "None"

    def insert_first(self, x):
        new_node = self.Node(x, None)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return x

    def insert_last(self, x):
        new_node = self.Node(x)
        if self.is_empty():
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1
        return x

    def remove_first(self):
        if self.is_empty():
            raise Exception("List is already Empty!")
        val = self.head.value
        if self.size == 1:
            self.head = None
        else:
            self.head = self.head.next
        self.size -= 1
        return val

    def remove_last(self):
        if self.is_empty():
            raise Exception("List is alredy Empty!")
        if self.size == 1:
            val = self.head.value
            self.head = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            val = curr.next.value
            curr.next = None
        self.size -= 1
        return val

    def insert(self, x, pos):
        if pos < 1 or pos > self.size + 1:
            raise Exception("Invalid Position!")
        if pos == 1:
            return self.insert_first(x)
        elif pos == self.size + 1:
            return self.insert_last(x)
        else:
            new_node = self.Node(x)
            curr = self.head
            c = 1
            while c != pos - 1:
                curr = curr.next
                c += 1
            new_node.next = curr.next
            curr.next = new_node
            self.size += 1
        return x

    def remove(self, pos):
        if self.is_empty():
            raise Exception("List is already Empty!")
        if pos < 1 or pos > self.size:
            raise Exception("Invalid Position!")
        if pos == 1:
            return self.remove_first()
        elif pos == self.size:
            return self.remove_last()
        else:
            curr = self.head
            c = 1
            while c != pos - 1:
                curr = curr.next
                c += 1
            to_delete = curr.next
            value = to_delete.value
            curr.next = to_delete.next
            self.size -= 1
            return value


ll = SinglyLinkedList()
ll.insert_first(3)
ll.insert_first(2)
ll.insert_first(1)
ll.insert_last(1)
ll.insert_last(2)
ll.insert_last(3)
print("Initial list:", ll)
print("Size:", ll.size)

# Test insert at various positions
print("\n--- Testing insert ---")
ll.insert(99, 1)  # Insert at beginning
print("After insert(99, 1):", ll)
print("Size:", ll.size)

ll.insert(88, 4)  # Insert in middle
print("After insert(88, 4):", ll)
print("Size:", ll.size)

ll.insert(77, ll.size + 1)  # Insert at end
print("After insert(77, end):", ll)
print("Size:", ll.size)

# Test remove at various positions
print("\n--- Testing remove ---")
val = ll.remove_first()
print(f"Removed first ({val}):", ll)
print("Size:", ll.size)

val = ll.remove_last()
print(f"Removed last ({val}):", ll)
print("Size:", ll.size)

val = ll.remove(3)  # Remove from middle
print(f"Removed at pos 3 ({val}):", ll)
print("Size:", ll.size)
