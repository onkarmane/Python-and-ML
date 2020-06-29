# To implement stack using linked list
#Class to represent node
class stacknode():
#Constructor to initialize node
      def __init__(self,data):
          self.data = data
          self.next = None

class stack():

#Constructor to initialize root
      def __init__(self):
         self.root = None

      def isempty(self):
            return True if self.root is None else  False

      def push(self,data):
        newnode = stacknode(data)
        newnode.next = self.root
        self.root = newnode
        print(str(data)+" pushed to stack")

      def pop(self):
            if self.isempty():
                return  float("-inf")
            temp = self.root
            self.root = self.root.next
            popped = temp.data
            return popped
# Driver program to test above class  
stack = stack() 
stack.push(10)         
stack.push(20) 
stack.push(30) 
  
print ("%d popped from stack" %(stack.pop())) 
    

    
