from collections import deque


# Tree represented using an adjacency list
tree = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': []
}


def bfs(start, goal):
    queue = deque([start])
    visited = set([start])

    print("Breadth First Search:")

    while queue:
        current = queue.popleft()

        print(current, end=" ")

        # Stop when goal is reached
        if current == goal:
            print("\nGoal node G achieved!")
            return

        for neighbor in tree[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print("\nGoal node not found.")


# Starting node = A
# Goal node = G
bfs('A', 'G')