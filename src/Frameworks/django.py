from django.shortcuts import render, redirect
from .models import Task

# Главная страница со списком задач
def index(request):
    """
    Отображает список всех задач.
    """
    tasks = Task.objects.all()  # Получаем все задачи из базы данных
    return render(request, 'tasks/index.html', {'tasks': tasks})

# Добавление новой задачи
def add_task(request):
    """
    Обрабатывает добавление новой задачи.
    """
    if request.method == 'POST':
        content = request.POST['content']  # Получаем текст задачи из формы
        Task.objects.create(content=content)  # Создаем новую задачу
    return redirect('index')  # Перенаправляем на главную страницу

# Отметка задачи как выполненной
def complete_task(request, task_id):
    """
    Отмечает задачу как выполненную.
    :param task_id: ID задачи
    """
    task = Task.objects.get(id=task_id)  # Находим задачу по ID
    task.done = True  # Помечаем как выполненную
    task.save()  # Сохраняем изменения
    return redirect('index')  # Перенаправляем на главную страницу
