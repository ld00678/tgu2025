import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # начальные расстояния
    distances[start] = 0
    visited = set()
    queue = [(0, start)]  # (расстояние, вершина)

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# Пример графа
graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Кратчайшие расстояния от вершины", start_node)
for node, distance in distances.items():
    print(f"{node}: {distance}")