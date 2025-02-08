from flask import Flask, render_template, request, redirect, url_for

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Пример данных (можно заменить на подключение к базе данных)
tasks = []

# Маршрут для главной страницы
@app.route('/')
def index():
    """
    Главная страница приложения.
    Отображает список задач и форму для добавления новой задачи.
    """
    return render_template('index.html', tasks=tasks)

# Маршрут для добавления новой задачи (обрабатывает POST-запросы)
@app.route('/add', methods=['POST'])
def add_task():
    """
    Обрабатывает добавление новой задачи.
    Получает данные из формы и добавляет задачу в список.
    """
    task_content = request.form['content']  # Получаем текст задачи из формы
    tasks.append({'content': task_content, 'done': False})  # Добавляем задачу в список
    return redirect(url_for('index'))  # Перенаправляем пользователя на главную страницу

# Маршрут для отметки задачи как выполненной
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    """
    Отмечает задачу как выполненную.
    :param task_id: ID задачи (индекс в списке)
    """
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True  # Помечаем задачу как выполненную
    return redirect(url_for('index'))  # Перенаправляем на главную страницу

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)  # Запускаем сервер в режиме отладки