from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView

from .models import Task
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

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

class TaskListView(TemplateView):
    template_name = 'tasks/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tasks'] = Task.objects.all()

        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

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
