import heapq


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def dequeue(self):
        if self.is_empty():
            return None

        priority, item = heapq.heappop(self.queue)
        return item

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Priority Queue:")
        for priority, item in sorted(self.queue):
            print("Item:", item, "| Priority:", priority)


# Create priority queue
pq = PriorityQueue()

# Insert elements
pq.enqueue("Task A", 3)   
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)
pq.enqueue("Task D", 4)

# Display queue
pq.display()

print("\nRemoving elements according to priority:")

while not pq.is_empty():
    print(pq.dequeue())