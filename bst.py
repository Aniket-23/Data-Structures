class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> bool:
        newNode = Node(value=value)
        if self.root is None:
            self.root = newNode
            return True
        temp = self.root
        while True:
            if newNode.value == temp.value:
                return False
            if newNode.value < temp.value:
                if temp.left is None:
                    temp.left = newNode
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newNode
                    return True
                temp = temp.right

tree = BinarySearchTree()
tree.insert(2)
tree.insert(1)
tree.insert(3)

print(f"Root: {tree.root.value}")
print(f"Left node: {tree.root.left.value}")
print(f"Right node: {tree.root.right.value}")
