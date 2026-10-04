from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        # Undirected graph
        self.graph[u].append(v)
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

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Create graph
g = Graph()

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