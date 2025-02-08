def dfs(graph, start, visited=None):
    """
    Поиск в глубину (DFS).
    :param graph: Граф в виде словаря смежности.
    :param start: Начальная вершина.
    :param visited: Множество посещенных вершин.
    :return: Список посещенных вершин.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")  # Посещаем вершину
    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)
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
print("\nПоиск в глубину (DFS):")
dfs(graph, 'A')