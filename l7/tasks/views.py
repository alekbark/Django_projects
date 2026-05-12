from os import name

from django.shortcuts import render
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect


# PW16 #1 Выведите с помощью методов языка Python все «поля», т.е.
# параметры запроса.
# 2. Придумайте и опишите ситуацию, когда необходимо перенаправление.
# Перенаправляем на главную страницу когда в параметрах URL не указано имя "name"

def show_request(request):
    name = request.GET.get('name')
    if name:
        return HttpResponse(f"""
        METHOD: {request.method} <br>
        PATH: {request.path} <br><br>
    
        GET: {request.GET.dict()} <br>
        POST: {request.POST.dict()} <br><br>
    
        HEADERS: {dict(request.headers)} <br><br>
    
        META: {request.META}
        """)
    else:
        return HttpResponseRedirect('/tasks/')

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
