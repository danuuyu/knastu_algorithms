def bubble_sort(arr):
    """
    Пузырьковая сортировка.
    :param arr: Список элементов для сортировки.
    :return: Отсортированный список.
    """
    n = len(arr)
    for i in range(n):
        # Флаг для оптимизации: если за проход не было обменов, массив уже отсортирован
        swapped = False
        for j in range(0, n - i - 1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если не было обменов, выходим из цикла
        if not swapped:
            break
    return arr


# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
print("Пузырьковая сортировка:", bubble_sort(arr))