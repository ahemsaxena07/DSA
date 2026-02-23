class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >=  self.length:
            return None
        temp = self.head 
        for _ in range(index):
            temp = temp.next
        return temp.value
    
my_list = LinkedList(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.print_list()
print(my_list.get(2))