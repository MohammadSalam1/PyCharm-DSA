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

if __name__ == "__main__":
    # Create a new linked list
    ll = LinkedList()
    print("Initial list (should be empty):", ll.display())
    print("Initial length:", len(ll))
    print()

    # Add elements at the front
    ll.add_first(10)
    ll.add_first(20)
    ll.add_first(30)
    print("After adding at front (30, 20, 10):", ll.display())
    print("Length after add_first:", len(ll))
    print()

    # Add elements at the end
    ll.add_last(40)
    ll.add_last(50)
    print("After adding at end (40, 50):", ll.display())
    print("Length after add_last:", len(ll))
    print()

    # Search for values
    print("Search for 20:", ll.search(20))  # should be True
    print("Search for 99:", ll.search(99))  # should be False
    print()

    # Remove first element
    removed_first = ll.remove_first()
    print(f"Removed first element: {removed_first}")
    print("List after remove_first:", ll.display())
    print("Length now:", len(ll))
    print()

    # Remove last element
    removed_last = ll.remove_last()
    print(f"Removed last element: {removed_last}")
    print("List after remove_last:", ll.display())
    print("Length now:", len(ll))
    print()

    # Test removing until empty
    print("Removing everything...")
    while len(ll) > 0:
        print("Removed:", ll.remove_first())
    print("List after clearing:", ll.display())
    print("Final length:", len(ll))
