class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            #new_node.prev = None
            self.head = new_node
            self.tail = new_node
            return
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        new_node.prev = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            #new_node.prev = None
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def delete(self, index: int):
        if index >= len(self) or index < 0 or len(self)==0:
            raise IndexError("Index out of range!")
        
        elif index == 0:
            temp = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return temp.data

        elif index == len(self)-1:

            temp = self.tail
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
            return temp.data
        
        current = self.head
        cur_index = 0

        while cur_index != index:
            current = current.next
            cur_index+=1

        current.prev.next = current.next
        current.next.prev = current.prev

    def length(self):
        size = 0
        current = self.head
        while current is not None:
            current = current.next
            size+=1
        return size
    
    def __len__(self):
        return self.length()

    def print(self, reversed=False):
        if reversed:
            current = self.tail
            while current is not None:
                print(current.data)
                current = current.prev
            return
        
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next        

lista = DoublyLinkedList()
lista.push(1)
lista.print()
print("=============")
lista.push(2)
lista.print()
print("=============")
lista.push(3)
lista.print()
print(lista.tail.data, lista.head.data)

print("=============")
lista.delete(2)
lista.print()
print(lista.tail.prev.data, lista.head.next.data)
