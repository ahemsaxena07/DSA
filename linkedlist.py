head = {
    "value": 2,
    "next": 
    {
        "value": 11,
        "next": 
        {
            "value": 7,
            "next": 
            {
                "value": 4,
                "next": "none"
            }
        }
    }
}

print(head['next']['next']['value'])

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
my_linked_list = LinkedList(4)
print(my_linked_list.head.value)