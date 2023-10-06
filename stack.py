class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.top = newNode
        self.bottom = newNode
        self.height = 1

    def printStack(self) -> None:
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next



stack  = Stack(10)
stack.printStack()