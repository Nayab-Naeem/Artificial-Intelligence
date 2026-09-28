class Stack:                     #LIFO conept
    def __init__(self):
      self.stack=[]

    def push(self,item):
       self.stack.append(item)
       print(f"Pushed: {item}")

    def pop(self): 
       if not self.is_empty():
          return self.stack.pop()
       else:
          return "stack is empty"

    def peek(self):     # top
       if not self.is_empty():
          return self.stack[-1]    # access last item in the list, represesnts top 
       else:
          return "Stack is empty"

    def is_empty(self):
       return len(self.stack) == 0

    def display(self):
       print("Stack" , self.stack) 

#Testing
s = Stack()
s.push(6)
s.push(12)
s.push(17)               
s.display()
print("Top element: " , s.peek())

print ("Popped: ", s.pop())
s.display()
