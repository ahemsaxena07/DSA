# # # # # # class Node:
# # # # # #     def __init__(self, value):
# # # # # #         self.value = value
# # # # # #         self.next = None

# # # # # # class LinkedList:
# # # # # #     def __init__(self, value):
# # # # # #         new_node = Node(value)
# # # # # #         self.head = new_node
# # # # # #         self.tail = new_node
# # # # # #         self.length = 1

# # # # # #     def append(self, value):
# # # # # #         new_node = Node(value)
# # # # # #         if self.length == 0:
# # # # # #             self.head = new_node
# # # # # #             self.tail = new_node
# # # # # #         else:
# # # # # #             self.tail.next = new_node
# # # # # #             self.tail = new_node
# # # # # #         self.length += 1
# # # # # #         return True 
    
# # # # # #     def print_list(self):
# # # # # #         temp = self.head
# # # # # #         while temp is not None:
# # # # # #             print(temp.value)
# # # # # #             temp = temp.next

# # # # # #     def pop(self):
# # # # # #         if self.length == 0:
# # # # # #             return None
# # # # # #         temp = self.head 
# # # # # #         pre = self.head 
# # # # # #         while(temp.next):
# # # # # #             pre = temp 
# # # # # #             temp = temp.next
# # # # # #         self.tail = pre
# # # # # #         self.tail.next = None 
# # # # # #         self.length -= 1
# # # # # #         if self.length == 0:
# # # # # #             self.head = None
# # # # # #             self.tail = None
# # # # # #         return temp
    
# # # # # #     def prepand(self, value):
# # # # # #         new_node = Node(value)
# # # # # #         if self.length == 0:
# # # # # #             self.head = new_node
# # # # # #             self.tail = new_node
# # # # # #         else:
# # # # # #             new_node.next = self.head
# # # # # #             self.head = new_node
# # # # # #         self.length += 1
# # # # # #         return True
    
# # # # # #     def popfirst(self):
# # # # # #         if self.length == 0:
# # # # # #             return None
# # # # # #         temp = self.head
# # # # # #         self.head = self.head.next
# # # # # #         temp.next = None
# # # # # #         self.length -= 1
# # # # # #         if self.length == 0:
# # # # # #             self.tail = None
# # # # # #         return temp
    
# # # # # #     def get(self, index):
# # # # # #         if index < 0 or index > self.length:
# # # # # #             return None 
# # # # # #         temp = self.head 
# # # # # #         for _ in range(index):
# # # # # #             temp = temp.next
# # # # # #         return temp

    
    

# # # # # # my_list = LinkedList(0)

# # # # # # my_list.append(1) 
# # # # # # my_list.append(2)
# # # # # # my_list.prepand(3)
# # # # # # my_list.pop()
# # # # # # my_list.popfirst()
# # # # # # my_list.print_list()


# # # # # class Node:
# # # # #     def __init__(self, value):
# # # # #         self.value = value
# # # # #         self.next = None

# # # # # class LinkedList:
# # # # #     def __init__(self, value):
# # # # #         new_node = Node(value)
# # # # #         self.head = new_node
# # # # #         self.tail = new_node
# # # # #         self.length = 1

# # # # #     def append(self, value):
# # # # #         new_node = Node(value)
# # # # #         if self.length == 0:
# # # # #             self.head = new_node
# # # # #             self.tail = new_node
# # # # #         else:
# # # # #             self.tail.next = new_node
# # # # #             self.tail = new_node
# # # # #         self.length += 1
# # # # #         return True
    
# # # # #     def print_list(self):
# # # # #         temp = self.head 
# # # # #         while temp is not None:
# # # # #             print(temp.value)
# # # # #             temp = temp.next

# # # # #     def pop(self):
# # # # #         if self.length == 0:
# # # # #             return None
# # # # #         temp = self.head 
# # # # #         pre = self.head 
# # # # #         while(temp.next):
# # # # #             pre = temp 
# # # # #             temp = temp.next
# # # # #         self.tail = pre 
# # # # #         self.tail.next = None
# # # # #         self.length -= 1
# # # # #         if self.length == 0:
# # # # #             self.head = None
# # # # #             self.tail = None
# # # # #         return temp
    
# # # # #     def prepand(self, value):
# # # # #         new_node = Node(value)
# # # # #         if self.length == 0:
# # # # #             self.head = new_node
# # # # #             self.head = new_node
# # # # #         else:
# # # # #             new_node.next = self.head
# # # # #             self.head = new_node
# # # # #         self.length += 1
# # # # #         return True 
    
# # # # #     def popfirst(self):
# # # # #         if self.length == 0:
# # # # #             return None
# # # # #         temp = self.head
# # # # #         self.head = self.head.next
# # # # #         temp.next = None
# # # # #         self.length -= 1
# # # # #         if self.length == 0:
# # # # #             self.tail = None
# # # # #         return temp
    
# # # # #     def get(self, index):
# # # # #         if index < 0 or index > self.length:
# # # # #             return None
# # # # #         temp = self.head
# # # # #         for _ in range(index):
# # # # #             temp = temp.next 
# # # # #         return temp 

# # # # class Node:
# # # #     def __init__(self, value):
# # # #         self.value = value
# # # #         self.next = None

# # # # class LinkedList:
# # # #     def __init__(self, value):
# # # #         new_node = Node(value)
# # # #         self.head = new_node
# # # #         self.tail = new_node
# # # #         self.length = 1

# # # #     def append(self, value):
# # # #         new_node = Node(value)
# # # #         if self.length == 0:
# # # #             self.head = new_node
# # # #             self.tail = new_node
# # # #         else:
# # # #             self.tail.next = new_node
# # # #             self.tail = new_node
# # # #         self.length += 1
# # # #         return True
    

# # # #     def print_list(self):
# # # #         temp = self.head
# # # #         while temp is not None:
# # # #             print(temp.value)
# # # #             temp = temp.next 

# # # #     def pop(self):
# # # #         if self.length == 0:
# # # #             return None
# # # #         temp = self.head
# # # #         pre = self.head
# # # #         while(temp.next):
# # # #             pre = temp
# # # #             temp = temp.next
# # # #         self.tail = pre
# # # #         self.tail.next = None
# # # #         self.length -= 1
# # # #         if self.length == 0:
# # # #             self.head = None
# # # #             self.tail = None
# # # #         return temp
    
# # # #     def prepand(self, value):
# # # #         new_node = Node(value)
# # # #         if self.length == 0:
# # # #             self.head = new_node
# # # #             self.tail = new_node
# # # #         else:
# # # #             new_node.next = self.head
# # # #             self.head = new_node
# # # #         self.length += 1
# # # #         return True 
    
# # # #     def firstpop(self):
# # # #         if self.length == 0:
# # # #             return None
# # # #         temp = self.head 
# # # #         self.head = self.head.next
# # # #         temp.next = None
# # # #         self.length -= 1
# # # #         if self.length == 0:
# # # #             self.tail = None
# # # #         return temp
    
# # # #     def get(self, index):
# # # #         if index < 0 or index > self.length:
# # # #             return None
# # # #         temp = self.head
# # # #         for _ in range(index):
# # # #             temp = temp.next
# # # #         return temp
    
# # # #     def set(self, index, value):
# # # #         temp = self.get(index)
# # # #         if temp:
# # # #             temp.value = value
# # # #             return True
# # # #         return False


# # # class Node:
# # #     def __init__(self, value):
# # #         self.value = value
# # #         self.next = None

# # # class LinkedList:
# # #     def __init__(self, value):
# # #         new_node = Node(value)
# # #         self.head = new_node
# # #         self.tail = new_node
# # #         self.length = 1

# # #     def append(self, value):
# # #         new_node = Node(value)
# # #         if self.length == 0:
# # #             self.head = new_node
# # #             self.tail = new_node
# # #         else:
# # #             self.tail.next = new_node
# # #             self.tail = new_node
# # #         self.length += 1
# # #         return True
    
# # #     def print_list(self):
# # #         temp = self.head
# # #         while temp is not None:
# # #             print(temp.value)
# # #             temp = temp.next

# # #     def pop(self):
# # #         if self.length == 0:
# # #             return None
# # #         temp = self.head
# # #         pre = self.head
# # #         while(temp.next):
# # #             pre = temp
# # #             temp = temp.next
# # #         self.tail = pre
# # #         self.tail.next = None
# # #         self.length -= 1
# # #         if self.length == 0:
# # #             self.head = None
# # #             self.tail = None
# # #         return temp 
    
# # #     def prepand(self, value):
# # #         new_node = Node(value)
# # #         if self.length == 0: 
# # #             self.head = new_node
# # #             self.tail = new_node
# # #         else:
# # #             new_node.next = self.head
# # #             self.head = new_node
# # #         self.length += 1
# # #         return True
    
# # #     def popfirst(self):
# # #         if self.length == 0:
# # #             return None
# # #         temp = self.head 
# # #         self.head = self.head.next
# # #         temp.next = None
# # #         self.length -= 1
# # #         if self.length == 0:
# # #             self.tail = None
# # #         return temp

# # #     def get(self, index):
# # #         if index< 0 or index > self.length:
# # #             return None
# # #         temp = self.head
# # #         for _ in range(index):
# # #             temp = temp.next
# # #         return temp

# # #     def insert(self, index, value):
# # #         if index < 0 or index > self.length:
# # #             return False
# # #         if index == 0:
# # #             return self.prepand(value)
# # #         if index == self.length:
# # #             return self.append(value)
# # #         new_node = Node(value)
# # #         temp = self.get(index - 1)
# # #         new_node.next = temp
# # #         temp = temp.next
# # #         self.length += 1
# # #         return True


# # class Node:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None

# # class LinkedList:
# #     def __init__(self, value):
# #         new_node = Node(value)
# #         self.head = new_node
# #         self.tail = new_node
# #         self.length = 1

# #     def append(self, value):
# #         new_node = Node(value)
# #         if self.length == 0:
# #             self.head = new_node
# #             self.tail = new_node
# #         else:
# #             self.tail.next = new_node
# #             self.tail = new_node
# #         self.length += 1
# #         return True
    
# #     def print_list(self):
# #         temp = self.head
# #         while temp is not None:
# #             print(temp.value)
# #             temp = temp.next

# #     def pop(self, value):
# #         if self.length == 0:
# #             return None
# #         temp = self.head
# #         pre = self.head
# #         while(temp.next):
# #             pre = temp
# #             temp = temp.next
# #         self.tail = pre
# #         self.tail.next = None
# #         self.length -= 1
# #         if self.length == 0:
# #             self.head = None
# #             self.tail = None
# #         return temp 
    
# #     def prepand(self, value):
# #         new_node = Node(value)
# #         if self.length == 0:
# #             self.head = new_node
# #             self.tail = new_node
# #         else:
# #             new_node.next = self.head
# #             self.head = new_node
# #         self.length += 1
# #         return True 
    
# #     def firstpop(self):
# #         if self.length == 0:
# #             return None
# #         temp = self.head
# #         self.head = self.head.next
# #         temp.next = None
# #         self.length -= 1
# #         if self.length == 0:
# #             self.tail = None
# #         return temp
    
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True
    
#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre = self.head
#         while(temp.next):
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         self.length -= 1
#         return temp
    
#     def prepand(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True
    
#     def firstpop(self, value):
#         if self.length == 0: 
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp 
    
#     def get(self, index):
#         if index < 0 or index > self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.value
#         return temp
    
#     def set(self, index, value):
#         temp = self.get(index)
#         if temp.next:
#             temp = temp.value
#             return True
#         return False
    
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return False
#         if index == 0:
#             return self.prepand(value)
#         if index == self.length:
#             return self.append(value)
#         new_node = Node(value)
#         temp = self.get(index - 1)
#         new_node.next = temp
#         temp = temp.next
#         self.length += 1
#         return True


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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def pop(self, value):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp 
    
    def prepand(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.value
        return temp 
    
    def set(self, index, value):
        temp = self.get(value)
        if temp.next:
            temp = temp.value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepand(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp
        temp = temp.next
        self.length += 1
        return temp
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp