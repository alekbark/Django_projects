from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Task
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime



# PW16 --------------------------------------------------------------------
# 1. Выведите с помощью методов языка Python все «поля», т.е.
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

# HW16 --------------------------------------------------------------------
# 1. Выполните перенаправление в случае отсутствия «логина» пользователя на
# любую другую страницу.
# Добавил форму с вводом логина

# 2. Залогируйте в любой текстовый файл данные с запроса.

def protected_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')

# здесь записывается лог
        with open('log.txt', 'a') as f:
            f.write(f"""
TIME: {datetime.now()} 
METHOD: {request.method} 
PATH: {request.path} 
GET: {request.GET.dict()} 
POST: {request.POST.dict()} 
-------------------------- 
""")

        if not login:
            return HttpResponse("Введите логин")

        return HttpResponse(f"""
            <h2>Добро пожаловать, {login}</h2>
            <meta http-equiv="refresh" content="3;url=/tasks/">
        """)

    return render(request, 'tasks/login.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(title=title, description=description)

        return redirect('/tasks/')

    return render(request, 'tasks/task_create.html')

def task_update(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':

        task.title = request.POST.get('title')
        task.description = request.POST.get('description')

        task.save()

        return redirect('/tasks/')

    return render(request, 'tasks/task_update.html', {'task': task})

@require_POST
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('/tasks/')