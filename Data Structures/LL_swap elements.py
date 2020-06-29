class Node(object):
    def __init__(self, data=None):
        self.data = data
    
        
class LinkedList():
    def __init__(self,head = None):
                self.head = None
                
# Function to insert a new node at the beginning 
    def push(self, new_data):
            new_node = Node(new_data) 
            new_node.next = self.head 
            self.head = new_node 
        
    def search(self,data):
            current = self.head
            prev = None
            if current == None:
                print("Empty list")
            while current:
                if current.data == data:
                    return prev,current
                else:
                    
                    current = current.next
                    prev = current
    
       
        
        
        
  
                   
                
# Utility function to print the linked LinkedList 
    def printList(self): 
            temp = self.head 
            while(temp): 
                print (" %d " ,temp.data)
                temp = temp.next
            

  
llist = LinkedList()
llist.push(1) 
llist.push(2) 
llist.push(3) 
llist.push(4) 
llist.push(5)
llist.push(6)
llist.push(7)
llist.push(8)
llist.printList()
llist.swap(7,5)
llist.printList()







