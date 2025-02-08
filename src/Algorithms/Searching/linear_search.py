def linear_search(arr, target):
    """
    Линейный поиск.
    :param arr: Список элементов.
    :param target: Искомый элемент.
    :return: Индекс элемента, если он найден, иначе -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
print("Линейный поиск: индекс элемента", target, "=", linear_search(arr, target))