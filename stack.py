class Node:
    def __init__(self,value):
        self.next = None
        self.value = value


class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        # while temp is not None:
        for _ in range(self.height):
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp

        



stack = Stack(6)
stack.push(7)
stack.push(8)
stack.pop()

stack.print_stack()
    
