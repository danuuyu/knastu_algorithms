from collections import deque

def bfs(graph, start):
    """
    Поиск в ширину (BFS).
    :param graph: Граф в виде словаря смежности.
    :param start: Начальная вершина.
    :return: Список посещенных вершин.
    """
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")  # Посещаем вершину
            visited.add(vertex)
            # Добавляем соседей в очередь
            queue.extend(graph[vertex] - visited)
    return visited


# Пример использования
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
print("Поиск в ширину (BFS):")
bfs(graph, 'A')