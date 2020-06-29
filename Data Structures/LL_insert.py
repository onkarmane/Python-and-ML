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
        
    def insert(self, data):
        current = self.head
        next = current.next
        if current == None:
            print("Empty list")
        while current:
            if current.data == data:
               current.next = neww
               neww.next = next
               
            else:
                current = current.next
                next = current.next
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
neww = Node(25)
llist.insert(8) 
print ("\nLinked List after insertion at position 3: ")
llist.printList()
