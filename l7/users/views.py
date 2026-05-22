from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import redirect
from .models import User

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email']
    template_name = 'users/user_form.html'
    success_url = '/users/'

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User

def find_user(request):
    user_id = request.GET.get('user_id')
    return redirect(f'/users/{user_id}/')