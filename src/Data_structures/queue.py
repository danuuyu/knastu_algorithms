from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()  # Используем deque для реализации очереди

    def enqueue(self, data):
        """Добавление элемента в конец очереди."""
        self.queue.append(data)

    def dequeue(self):
        """Удаление и возврат элемента из начала очереди."""
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        """Проверка, пуста ли очередь."""
        return len(self.queue) == 0

    def size(self):
        """Возврат количества элементов в очереди."""
        return len(self.queue)

# Пример использования
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Вывод: 1
print(queue.size())  # Вывод: 1