from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, CreateView, UpdateView, DetailView, DeleteView,
    MonthArchiveView, YearArchiveView, TodayArchiveView, RedirectView
)
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

class TaskRedirectView(RedirectView):
    pattern_name = 'task_list'

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
        return redirect('go_to_tasks')

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

class TaskListView(ListView):
    model = Task
    paginate_by = 10

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'tasks/task_create.html'
    success_url = '/tasks/'

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'tasks/task_update.html'
    success_url = '/tasks/'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = '/tasks/'

class TaskMonthArchiveView(MonthArchiveView):
    model = Task
    template_name = 'tasks/month_archive.html'
    date_field = 'created_at'
    month_format = '%m'

class TaskYearArchiveView(YearArchiveView):
    model = Task
    template_name = 'tasks/year_archive.html'
    date_field = 'created_at'
    year_format = '%Y'
    make_object_list = True

class TaskTodayArchiveView(TodayArchiveView):
    model = Task
    template_name = 'tasks/today_archive.html'
    date_field = 'created_at'
