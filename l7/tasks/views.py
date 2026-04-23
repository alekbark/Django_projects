from django.shortcuts import render

def task_list(request):
    return render(request, 'tasks/task_list.html')

def task_detail(request, id):
    return render(request, 'tasks/task_detail.html', {'id': id})

def task_create(request):
    return render(request, 'tasks/task_create.html')

def task_update(request, id):
    return render(request, 'tasks/task_update.html', {'id': id})

def task_delete(request, id):
    return render(request, 'tasks/task_delete.html', {'id': id})

def completed_tasks(request):
    return render(request, 'tasks/completed_tasks.html')

def active_tasks(request):
    return render(request, 'tasks/active_tasks.html')

def tasks_by_year(request, year):
    return render(request, 'tasks/tasks_by_year.html', {'year': year})

def tasks_by_month(request, year, month):
    return render(request, 'tasks/tasks_by_month.html', {'year': year, 'month': month})

def user_tasks(request, username):
    return render(request, 'tasks/user_tasks.html', {'username': username})

def task_list_paginated(request, page):
    return render(request, 'tasks/task_list_paginated.html', {'page': page})

def task_by_slug(request, slug):
    return render(request, 'tasks/task_by_slug.html', {'slug': slug})