#Delete middle element from stack using recursive funtion
class stack():
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def deletemid(st,n,curr):
#If stack is empty or all items are traversed
    if (st.isempty() or curr == n):
        return
#remove current item
    x = st.peek()
    st.pop()
#remove other items
    deletemid(st,n,curr+1)
#put all items back except middle
    if (curr != int(n/2)):
         st.push(x)

#Driver function to test above function
st = stack()
st.push('1') 
st.push('2') 
st.push('3') 
st.push('4') 
st.push('5') 
st.push('6') 
st.push('7')

deletemid(st, st.size(), 0)

#print after deletion of middle
while (st.isempty == False):
        p = st.peek()
        st.pop()
        print(str(p) + " ", end="")
    
    




   
        
