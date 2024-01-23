class Node:
    def __init__(self, data):
        self.address = None
        self.data = data

first_node = Node(13)

class Linked_list:
    def __init__(self):
        self.head = None
    
    def insertion_at_first(self,input_data):
        temp_head = linked_list_object.head
        self.head = Node(input_data)
        self.head.address = temp_head
        
    def insertion_at_last(self,input_data):
        last_node  = linked_list_object.head
        while(last_node.address != None):
            last_node = last_node.address
        last_node.address = Node(input_data)
        
    def printing_linked_list(self):
        temp_node = linked_list_object.head
        print(temp_node.address)
        while(temp_node.address != None ):
            print(temp_node.data)
            temp_node = temp_node.address
        print(temp_node.data)
            
linked_list_object = Linked_list()
linked_list_object.head = first_node

linked_list_object.insertion_at_first(9)
linked_list_object.insertion_at_first("this is latest")
linked_list_object.insertion_at_first("NOOO, this is latest data")
linked_list_object.insertion_at_last(10000)
linked_list_object.insertion_at_last(1222222)
linked_list_object.printing_linked_list()
