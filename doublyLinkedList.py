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

myList = DoublyLinkedList(1)
myList.printList()