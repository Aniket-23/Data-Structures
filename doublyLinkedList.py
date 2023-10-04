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

myList = DoublyLinkedList(1)
myList.append(3)
myList.append(5)
myList.printList()