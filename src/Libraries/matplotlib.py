import matplotlib.pyplot as plt
import numpy as np

# Создание данных
x = np.linspace(0, 10, 100)  # 100 точек от 0 до 10
y = np.sin(x)  # Синусоида

# Построение графика
plt.plot(x, y, label='sin(x)')
plt.title("График синуса")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.legend()
plt.grid(True)
plt.show()

# Гистограмма
data = np.random.randn(1000)  # 1000 случайных чисел
plt.hist(data, bins=30, alpha=0.7, color='blue')
plt.title("Гистограмма случайных данных")
plt.xlabel("Значения")
plt.ylabel("Частота")
plt.show()

# Столбчатая диаграмма
categories = ['Категория A', 'Категория B', 'Категория C']
values = [10, 20, 15]
plt.bar(categories, values, color='green')
plt.title("Столбчатая диаграмма")
plt.xlabel("Категории")
plt.ylabel("Значения")
plt.show()