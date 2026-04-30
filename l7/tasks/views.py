from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, id):
    return render(request, 'tasks/task_detail.html', {'id': id})

def task_create(request):
    return render(request, 'tasks/task_create.html')

def task_update(request, id):
    return render(request, 'tasks/task_update.html', {'id': id})

def task_delete(request, id):
    return render(request, 'tasks/task_delete.html', {'id': id})
