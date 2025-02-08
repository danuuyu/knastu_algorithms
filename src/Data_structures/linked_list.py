class Node:
    def __init__(self, data):
        self.data = data  # Данные, хранящиеся в узле
        self.next = None  # Ссылка на следующий узел

class LinkedList:
    def __init__(self):
        self.head = None  # Начало списка

    def append(self, data):
        """Добавление элемента в конец списка."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Добавление элемента в начало списка."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        """Вывод всех элементов списка."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Пример использования
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.prepend(0)
ll.print_list()  # Вывод: 0 -> 1 -> 2 -> None