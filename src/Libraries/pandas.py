import pandas as pd

# Создание DataFrame
data = {
    'Имя': ['Алексей', 'Мария', 'Иван'],
    'Возраст': [25, 30, 22],
    'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Доступ к столбцам
print("Имена:\n", df['Имя'])

# Фильтрация данных
filtered_df = df[df['Возраст'] > 25]
print("Люди старше 25 лет:\n", filtered_df)

# Добавление нового столбца
df['Зарплата'] = [50000, 60000, 45000]
print("DataFrame с зарплатой:\n", df)

# Сохранение в CSV
df.to_csv('data.csv', index=False)

# Загрузка из CSV
loaded_df = pd.read_csv('data.csv')
print("Загруженный DataFrame:\n", loaded_df)