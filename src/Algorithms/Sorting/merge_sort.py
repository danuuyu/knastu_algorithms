def merge_sort(arr):
    """
    Сортировка слиянием (Merge Sort).
    :param arr: Список элементов для сортировки.
    :return: Отсортированный список.
    """
    if len(arr) <= 1:
        return arr

    # Разделяем список на две половины
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Объединяем отсортированные половины
    return merge(left_half, right_half)


def merge(left, right):
    """
    Вспомогательная функция для слияния двух отсортированных списков.
    :param left: Левый отсортированный список.
    :param right: Правый отсортированный список.
    :return: Объединенный отсортированный список.
    """
    result = []
    i = j = 0

    # Слияние двух списков
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы (если один из списков длиннее)
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
print("Сортировка слиянием:", merge_sort(arr))