class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.top = newNode
        self.height = 1

    def printStack(self) -> None:
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value) -> None:
        newNode = Node(value)
        if self.height == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp



stack  = Stack(10)
stack.push(5)
stack.push(1)
stack.printStack()
print(f"Popped value: {stack.pop().value}")
stack.printStack()