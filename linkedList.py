# define a class to create a new node
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# define a class to work with the Linked lists
class LinkedList:
    # to create a new starting node
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def empty(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    # to append a new node if there is an existing Linked list, else create one with it
    def append(self, value) -> bool:
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return True
    
    def printList(self) -> None:
        if self.head is not None:
            temp = self.head

            while temp is not None:
                print(temp.value)
                temp = temp.next
        else:
            print("Linked list is empty")

    def pop(self) -> None:
        if self.head is None:
            print("Linked list empty. Nothing to pop")
        elif self.head == self.tail:
            print(f"{self.head.value} is popped")
            self.head = None
            self.tail = None
            self.length = 0
        else:
            temp = self.head
            pre = self.head
            while(temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            print(f"{temp.value} is popped")
            
    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def popFirst(self):
        if self.length == 0:
            print("Linked list is empty")
            return
        elif self.length == 1:
            print(f"{self.head.value} is popped")
            self.head = None
            self.tail = None
        else:
            print(f"{self.head.value} is popped")
            self.head = self.head.next
        self.length-=1

    def get(self, index):
        if index <= 0 or index >= self.length:
            print("Index out of bounds")
            return
        temp = self.head
        for i in range(index):
            temp = temp.next
        print(f"Element at index {index} = {temp.value}")

myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)
myLinkedList.get(1)