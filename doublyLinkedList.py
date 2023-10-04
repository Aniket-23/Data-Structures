class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def printList(self) -> None:
        temp = self.head
        print("Your doubly linked list:")
        while temp:
            print(f"{temp.value}")
            temp = temp.next

    def append(self, value) -> bool:
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp


myList = DoublyLinkedList(1)
myList.append(3)
myList.append(5)
myList.printList()
myList.pop()
myList.pop()
myList.printList()