def quick_sort(arr):
    """
    Быстрая сортировка (Quick Sort).
    :param arr: Список элементов для сортировки.
    :return: Отсортированный список.
    """
    if len(arr) <= 1:
        return arr
    # Выбираем опорный элемент (pivot)
    pivot = arr[len(arr) // 2]
    # Разделяем элементы на три группы: меньше, равно и больше pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Рекурсивно сортируем левую и правую части
    return quick_sort(left) + middle + quick_sort(right)


# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
print("Быстрая сортировка:", quick_sort(arr))