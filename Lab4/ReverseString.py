class Stack:
    def __init__(self):
        self.stack = []

    def push (self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()        
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

def reverse_string(text):
    s = Stack ()

    for char in text:
        s.push(char)        

    reversed_text = ""
    while not s.is_empty():
        reversed_text += s.pop()
    return reversed_text

#testing

my_string = "Hello"
print ("original" , my_string)
print("reversed" , reverse_string(my_string))    