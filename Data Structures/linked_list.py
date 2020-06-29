class Node(object):

    def __init__(self, data=None):
        self.data = data

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
# Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
        
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        if current == None:
            print("Empty list")
        while current and found is False:
            if current.data == data:
               current = current.next
               previous.next = current
               found = True
            else:
                previous = current
                current = current.next
# Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (" %d " ,temp.data)
            temp = temp.next
            
   

llist = LinkedList()

 
llist.push(7) 
llist.push(1) 
llist.push(3) 
llist.push(2) 
llist.push(8)
print ("Created Linked List: ",llist.printList())
llist.delete(3) 
print ("\nLinked List after Deletion at position 3: ")
llist.printList() 
