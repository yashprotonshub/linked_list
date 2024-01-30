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
        
    def insert_at_particular_position(self, index , input_data ):
        c=0
        temp_node = linked_list_object.head
        while(c!=2):
            temp_node = temp_node.address
            c+=1
        new_node = Node(input_data)
        storing_temp_node_address = temp_node.address
        temp_node.address=new_node
        new_node.address = storing_temp_node_address
        
    def update_node_of_linked_list(self, index, updated_data):
        c=0
        temp_node = linked_list_object.head
        while(c!=index-1):
            temp_node = temp_node.address
            c+=1
        temp_node.data = updated_data
        
        
        
linked_list_object = Linked_list()
linked_list_object.head = first_node

linked_list_object.insertion_at_first(9)
linked_list_object.insertion_at_first("this is latest")
linked_list_object.insertion_at_first("NOOO, this is latest data")
linked_list_object.insertion_at_last(10000)
linked_list_object.insertion_at_last(1222222)
linked_list_object.insert_at_particular_position(int(input("enter index where you want to insert the linked list "  )), input("enter data you want to input : "))
linked_list_object.update_node_of_linked_list(int(input("enter index of linked list : ")), input("enter data you want to update for linked list :"))
linked_list_object.printing_linked_list()