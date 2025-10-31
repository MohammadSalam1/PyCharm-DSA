'''
Build a Stack and Queue using LinkedList instead of Python lists.
'''
class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.link = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, element):
        new_node = Node(element)
        new_node.link = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def add_last(self, element):
        new_tail = Node(element)

        if self.head is None:
            self.head = new_tail
            self.tail = new_tail

        else:
            self.tail.link = new_tail
            self.tail = new_tail

        self.size += 1

    def remove_first(self):
        if self.head is None:
            return None
        rem_data = self.head.data
        self.head = self.head.link
        if self.head is None:
            self.tail = None

        self.size -= 1
        return rem_data


    def remove_last(self):
        if self.head is None:
            return None

        if self.head == self.tail:
            single_data = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return single_data

        current = self.head
        while current.link != self.tail:
            current = current.link

        data = self.tail.data
        current.link = None
        self.tail = current

        self.size -= 1
        return data


    def search(self, target):
        if self.head is None:
            return None

        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.link

        return False

    def display(self):
        elements = []

        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.link

        return elements

    def __len__(self):
        return self.size
class Stack:
    def __init__(self):
        self._list = LinkedList()

    def push(self, item):
        self._list.add_first(item)  # add at head (O(1))

    def pop(self):
        return self._list.remove_first()  # remove from head (O(1))

    def peek(self):
        return None if self._list.head is None else self._list.head.data

    def is_empty(self):
        return len(self._list) == 0

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return f"Stack(top→bottom): {self._list.display()}"

class Queue:
    def __init__(self):
        self._list = LinkedList()

    def enqueue(self, item):
        self._list.add_last(item)  # O(1) because tail pointer is tracked

    def dequeue(self):
        return self._list.remove_first()  # O(1)

    def front(self):
        return None if self._list.head is None else self._list.head.data

    def is_empty(self):
        return len(self._list) == 0

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return f"Queue(front→back): {self._list.display()}"


if __name__ == "__main__":
    print("=== LINKED LIST TEST ===")
    ll = LinkedList()
    print("Initial list:", ll.display())
    print("Empty?", len(ll) == 0)
    print()

    # Add items
    ll.add_first(10)
    ll.add_first(20)
    ll.add_last(30)
    ll.add_last(40)
    print("List after adding elements:", ll.display())
    print("Length:", len(ll))
    print()

    # Remove items
    print("Removed first:", ll.remove_first())
    print("Removed last:", ll.remove_last())
    print("List after removals:", ll.display())
    print("Length now:", len(ll))
    print()

    # Search test
    print("Searching for 20:", ll.search(20))
    print("Searching for 99:", ll.search(99))
    print()

    print("=== STACK TEST ===")
    s = Stack()
    s.push("A")
    s.push("B")
    s.push("C")
    print(s)
    print("Peek:", s.peek())
    print("Pop:", s.pop())
    print(s)
    print("Is empty?", s.is_empty())
    print("Length:", len(s))
    print()

    print("=== QUEUE TEST ===")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print("Front:", q.front())
    print("Dequeue:", q.dequeue())
    print(q)
    print("Is empty?", q.is_empty())
    print("Length:", len(q))

