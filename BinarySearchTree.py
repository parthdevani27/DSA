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
    
    def __r_contains(self,node,value):
        if node == None:
            return False
        if node.value == value:
            return True
        if node.value > value:
            return self.__r_contains(node.left,value)
        if node.value < value:
            return self.__r_contains(node.right,value)

    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    

    def r_insert(self,value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root,value)

    def __r_insert(self,node,value):
        if node == None:
            return Node(value)
        if node.value > value:
            node.left = self.__r_insert(node.left,value)
        if node.value < value:
            node.right = self.__r_insert(node.right,value)
        return node
    
    def r_delete(self,value):
        self.__r_delete(self.root,value)

    def __r_delete(self,node,value):
        if node == None:
            return None
        if value < node.value:
            self.left = self.__r_delete(node.left,value)
        elif value > node.value:
            self.right = self.__r_delete(node.right,value)
        else:
            if node.left == None and node.right == None:
                return None
            elif node.left == None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                sub_tree_min = self.min_value(node.right)
                node.value = sub_tree_min
                node.right = self.__r_delete(node.right,sub_tree_min)
                return node
        return Node
    
    def min_value(self,node):
        while node.left is not None:
            node = node.left
        return node.value

tree = BinarySearchTree()
tree.r_insert(10)
tree.r_insert(8)
tree.r_insert(13)
tree.r_insert(11)
tree.r_insert(14)
tree.r_insert(30)
tree.r_insert(22)
tree.r_insert(27)
tree.r_insert(21)
tree.r_insert(24)
tree.r_insert(7)
tree.r_insert(9)

tree.r_delete(126)

# print(tree.r_contains(11))
print(tree.root.value)
print(tree.root.left.value,tree.root.right.value)
            



