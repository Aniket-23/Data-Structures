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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
            
    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index<0 or index>self.length:
            return False
        elif index==0:
            return self.prepend(value)
        elif index==self.length:
            return self.append(value)
        newNode=Node(value)
        temp=self.get(index-1)
        newNode.next=temp.next
        temp.next=newNode
        self.length+=1
        return True

myLinkedList = LinkedList(1)
myLinkedList.append(3)

print("Linked list before insertion:")
myLinkedList.printList()
myLinkedList.insert(1, 2)
print("Linked list after insertion:")
myLinkedList.printList()
myLinkedList.insert(0, 9)
print("Linked list after insertion at beginning:")
myLinkedList.printList()
myLinkedList.insert(4, 5)
print("Linked list after insertion at end:")
myLinkedList.printList()
myLinkedList.insert(10, 11)
print("Linked list after insertion out of range:")
myLinkedList.printList()