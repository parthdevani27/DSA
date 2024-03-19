class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None
        self.tail = pre
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepand(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        if self.length == 0:
            self.tail = None
        self.length -= 1
        return temp

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node
    
    def set_value(self,index,value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepand(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        pre_node = self.get(index - 1)
        new_node.next = pre_node.next   
        pre_node.next = new_node
        self.length += 1
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre_node =  self.get(index -1)
        node =  pre_node.next
        pre_node.next = node.next
        node.next = None
        self.length -= 1
        return node
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
            


ll = LinkedList(1) 
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.reverse()
ll.print_list()
print('lenght',ll.length)
# print(ll.get(0))
