import numpy as np

# Создание массива
arr = np.array([1, 2, 3, 4, 5])
print("Массив:", arr)

# Массив из нулей
zeros_arr = np.zeros(5)
print("Массив из нулей:", zeros_arr)

# Массив из единиц
ones_arr = np.ones(5)
print("Массив из единиц:", ones_arr)

# Массив с диапазоном
range_arr = np.arange(0, 10, 2)  # От 0 до 10 с шагом 2
print("Массив с диапазоном:", range_arr)

# Матрица (двумерный массив)
matrix = np.array([[1, 2], [3, 4]])
print("Матрица:\n", matrix)

# Операции с массивами
sum_arr = arr + 10  # Прибавление 10 к каждому элементу
print("Массив + 10:", sum_arr)

# Скалярное произведение
dot_product = np.dot(matrix, matrix)
print("Скалярное произведение матриц:\n", dot_product)