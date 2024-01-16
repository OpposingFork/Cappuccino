INF = float("inf")

def generate_path(start, goal, prev):
    path = []
    p = goal
    while p != start:
        path.append(p)
        if p not in prev:
            return []
        p = prev[p]
    path.append(start)
    path.reverse()
    return path

def dijkstra(graph, start, goal):
    Q = set(graph)
    dist = {v: INF for v in graph}
    dist[start] = 0
    prev = {}
 
    while Q:
        u = min(Q, key = lambda u: dist[u])
        Q.remove(u)
 
        for v in graph[u]:
            if v not in Q: continue
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
 
    path = generate_path(start, goal, prev)
    return path, dist[goal]