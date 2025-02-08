class HashTable:
    def __init__(self, size):
        self.size = size  # Размер хэш-таблицы
        self.table = [[] for _ in range(size)]  # Инициализация таблицы пустыми списками

    def _hash(self, key):
        """Хэш-функция для вычисления индекса."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Вставка пары ключ-значение в хэш-таблицу."""
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value  # Обновление значения, если ключ уже существует
                return
        self.table[index].append([key, value])  # Добавление новой пары ключ-значение

    def get(self, key):
        """Получение значения по ключу."""
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None  # Возврат None, если ключ не найден

    def delete(self, key):
        """Удаление пары ключ-значение по ключу."""
        index = self._hash(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return

# Пример использования
ht = HashTable(10)
ht.insert("key1", "value1")
ht.insert("key2", "value2")
print(ht.get("key1"))  # Вывод: value1
ht.delete("key1")
print(ht.get("key1"))  # Вывод: None