#Program to implement stack

#function to create stack
def createstack():
    stack = []        #stack as empty list
    return stack
def isempty(stack):
    return len(stack) == 0

#funtion to add items to stack
def push(stack,item):
    stack.append(item)
    print(str(item) + "  pushed to stack")

#function to remove item from stack
def pop(stack):
    if isempty(stack):
        return -1
    else:
        return stack.pop()
    
    
#Driver program to test program
stack = createstack()
push(stack,10)
push(stack,20)
push(stack,30)
push(stack,40)
print(str(pop(stack))+" popped from stack")
