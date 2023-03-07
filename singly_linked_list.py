class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        """Adiciona um elemento no início da lista"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        """Adiciona um elemento no final da lista"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current=current.next
        current.next = new_node

    def delete(self, index):
        """"Deleta e retorna o elemento do índice passado"""
        if index >= self.length() or index < 0:
            raise IndexError("Index out of range")

        cur_index = 0
        current = self.head
        previous = self.head

        if index == 0:
            self.head = current.next
            return current.data

        while True:
            if cur_index == index:
                if current.next is not None:
                    previous.next = current.next
                    return current.data
                
                previous.next = None
                return current.data
            
            previous = current
            current = current.next
            cur_index+=1


    def pop(self):
        """Deleta e retorna o último elemento da lista"""
        current = self.head
        previous = self.head
        while current.next is not None:
            previous = current
            current = current.next

        previous.next = None
        return current
    
    def length(self):
        cur = self.head
        size = 0
        while cur is not None:
            size+=1
            cur = cur.next
        return size

    def __len__(self):
        return self.length()

    def print(self):
        current = self.head
        while current!=None:
            print(current.data)
            current = current.next


lista = LinkedList()
lista.append(0)
lista.append(1)
lista.append(2)
lista.print()
print("============")
lista.delete(-1)
lista.print()
print("============")
lista.pop()
lista.print()
