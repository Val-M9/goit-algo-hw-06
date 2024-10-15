import heapq
from district import district


def dfs(graph, start, visited=None, path=None, parent=None):
    if visited is None:
        visited = set()
        path = []
    visited.add(start)
    if parent is not None:
        path.append((parent, start))
    for next in graph.neighbors(start):
        if next not in visited:
            dfs(graph, next, visited, path, start)
    return path


def bfs(graph, start):
    visited = set()
    queue = [start]
    path = []
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        for next in graph.neighbors(vertex):
            if next not in visited:
                visited.add(next)
                queue.append(next)
                path.append((vertex, next))
    return path


def dijkstra(graph, start):
    shortest_path = {vertex: float('infinity') for vertex in graph}
    shortest_path[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > shortest_path[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_path


dfs_path = dfs(district, 'Home')
bfs_path = bfs(district, 'Home')
shortest_path = dijkstra(district, 'Cinema')

print(f"DFS path: {dfs_path}")
print(f"BFS path: {bfs_path}")
print(f"Shortest path: {shortest_path}")
