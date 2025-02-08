class Stack:
    def __init__(self):
        self.stack = []  # Используем список для хранения элементов стека

    def push(self, data):
        """Добавление элемента на вершину стека."""
        self.stack.append(data)

    def pop(self):
        """Удаление и возврат элемента с вершины стека."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        """Возврат элемента с вершины стека без его удаления."""
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        """Проверка, пуст ли стек."""
        return len(self.stack) == 0

    def size(self):
        """Возврат количества элементов в стеке."""
        return len(self.stack)

# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Вывод: 2
print(stack.peek())  # Вывод: 1
print(stack.size())  # Вывод: 1