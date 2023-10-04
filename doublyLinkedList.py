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
    
    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        return True
    
    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            if index < self.length/2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length-1, index, -1):
                    temp = temp.prev
            return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            newNode = Node(value)
            before = self.get(index-1)
            after = before.next
            newNode.prev = before
            newNode.next = after
            before.next = newNode
            after.prev = newNode
            self.length += 1
            return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.popFirst()
        elif index == self.length-1:
            return self.pop()
        else:
            temp = self.get(index)
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.prev = None
            temp.next = None
            return temp


myList = DoublyLinkedList(1)
myList.append(3)
myList.append(5)
myList.printList()
myList.insert(3, 2)
myList.printList()
myList.insert(2, 4)
myList.printList()
print()
print(myList.remove(2).value)