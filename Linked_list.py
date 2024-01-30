class Node:
    def __init__(self, data):
        self.address = None
        self.data = data

first_node = Node(1)

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
        
    def removing_first_node_of_linked_list(self):
        linked_list_object.head = linked_list_object.head.address
        
    def removing_last_node_of_linked_list(self):
        temp_node = linked_list_object.head
        while(temp_node.address !=None):
            current_node = temp_node 
            temp_node = temp_node.address
        current_node.address = None
        
    def removing_node_at_particular_index(self,index):
        
        current_node = linked_list_object.head
        previous_node = current_node  
        c=0
        while(c!=index):
            previous_node = current_node 
            current_node = current_node.address
            c+=1
        previous_node.address = current_node.address 
    
    def length_of_linked_list(self):
        current_node = linked_list_object.head
        c=1
        while(current_node.address != None):
            current_node = current_node.address
            c+=1
        return c
    
        
        
        
linked_list_object = Linked_list()
linked_list_object.head = first_node

second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
fifth_node = Node(5)

linked_list_object.head.address = second_node 
second_node.address = third_node
third_node.address = fourth_node
fourth_node.address = fifth_node
returned_value = linked_list_object.length_of_linked_list()
print("Length of the Linked List is : ",returned_value)
