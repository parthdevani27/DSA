class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        if new_node.value == temp.value:
            return False
        while temp != new_node:
            if temp.value > new_node.value:
                if temp.left == None:
                    temp.left = new_node
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                temp = temp.right
        return True

    def contains(self,value):
        temp = self.root
        while temp is not None:
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            else:
                return True
        return False
        

tree = BinarySearchTree()
tree.insert(3)
tree.insert(5)
tree.insert(4)
tree.insert(8)

print(tree.contains(2))
            



