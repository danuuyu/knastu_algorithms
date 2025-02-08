def binary_search(arr, target):
    """
    Бинарный поиск.
    :param arr: Отсортированный список элементов.
    :param target: Искомый элемент.
    :return: Индекс элемента, если он найден, иначе -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Пример использования
arr = [11, 12, 22, 25, 34, 64, 90]
target = 22
print("Бинарный поиск: индекс элемента", target, "=", binary_search(arr, target))