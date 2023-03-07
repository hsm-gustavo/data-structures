class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current
        new_node.next = None

    def push(self, data):
        new_node = Node(data)
        
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        new_node.prev = None

    def delete(self, index):
        if index >= len(self) or index < 0:
            raise IndexError("Index out of range!")
        
        cur_index = 0
        current = self.head

        if index == 0:
            self.head = self.head.next
            self.head.next.prev = None
            return current.data

        while True:
            if cur_index == index:
                current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                return current.data

            current = current.next
            cur_index+=1

    def pop(self):
        current = self.head

        while current.next is not None:
            current = current.next

        current.prev.next = None
        return current

    def print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def length(self):
        current = self.head
        size = 0
        while current is not None:
            size+=1
            current = current.next
        
        return size

    def __len__(self):
        return self.length()


lista =  DoublyLinkedList()
lista.append(1)

""" lista.append(2)
lista.append(3) """

lista.print()
print("============")
lista.pop()
lista.print()