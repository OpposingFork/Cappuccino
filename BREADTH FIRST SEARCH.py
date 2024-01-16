from collections import deque

def bfs(graph, source):
  queue = deque([source]) 
  visited = {source}
  
  while queue:
    current = queue.popleft()
    print(current)
    
    for neighbor in graph[current]:
      if neighbor not in visited:
        queue.append(neighbor)
        visited.add(neighbor)

# Graph as a dictionary 
graph = {'A': ['B', 'C'],
         'B': ['D', 'E'], 
         'C': ['F'],
         'D': ['G'], 
         'E': ['F'],
         'F': [],
         'G': []}

bfs(graph, 'A')