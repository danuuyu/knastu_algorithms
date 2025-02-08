import heapq

def dijkstra(graph, start):
    """
    Алгоритм Дейкстры для поиска кратчайших путей.
    :param graph: Граф в виде словаря смежности с весами.
    :param start: Начальная вершина.
    :return: Словарь с кратчайшими расстояниями до всех вершин.
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Пример использования
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_vertex = 'A'
print("\nАлгоритм Дейкстры:")
print("Кратчайшие расстояния от вершины", start_vertex, ":", dijkstra(graph, start_vertex))