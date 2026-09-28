class Queue:                    #FIFO
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)
        print(f"Enqueued {item}")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else: 
            return "Queue is Empty!"

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is Empty"    
        
    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:" , self.queue)

 #Testing 
q = Queue()
q.enqueue(6)
q.enqueue(12)
q.enqueue(17)
q.display()

print("Front : " , q.front())   
print ("Dequeued : " , q.dequeue() )
q.display()
