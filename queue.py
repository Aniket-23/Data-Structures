class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1

    def printQueue(self) -> None:
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value) -> None:
        newNode = Node(value)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp



queue = Queue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.printQueue()
print()
print(queue.dequeue().value)
print()
queue.printQueue()