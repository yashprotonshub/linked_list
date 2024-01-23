class Node:
    def __init__(self, data):
        self.address = None
        self.data = data

first_node = Node(13)

class Linked_list:
    def __init__(self):
        self.head = None
    
    def insertion_at_front(self,input_data):
        temp_head = linked_list_object.head
        self.head = Node(input_data)
        self.head.address = temp_head
        
linked_list_object = Linked_list()
linked_list_object.head = first_node

linked_list_object.insertion_at_front(9)
print(linked_list_object.head.address.address)


