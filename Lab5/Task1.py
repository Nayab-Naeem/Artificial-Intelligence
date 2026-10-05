from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}   #stores graph as adjacent list 

    def add_edge(self, u, v):    #adding edges
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        # Undirected graph 
        self.graph[u].append(v)         # dono sides se edge connect hoga
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque()

        # Mark starting node as visited
        visited.add(start)
        queue.append(start)

        print("Breadth First Search Traversal:")

        while queue:
            vertex = queue.popleft() 
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:      #checking neighbours if they r in visited list , if not then added
                if neighbor not in visited:         
                    visited.add(neighbor)
                    queue.append(neighbor)


# Create graph
g = Graph()     # graph class ka ek object bna rhe jiska naam g ha 

# Add edges according to the given graph
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(4, 1)
g.add_edge(4, 3)
g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(3, 2)

# Perform BFS starting from vertex 0
g.bfs(0)