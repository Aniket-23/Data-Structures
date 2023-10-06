class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.first = newNode
        self.last = newNode

    def printQueue(self) -> None:
        temp = self.first
        if temp:
            print(temp.value)
            temp = temp.next



queue = Queue(10)
queue.printQueue()