from django.urls import path
from .views import UserCreateView, UserListView, UserDetailView, find_user

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='user_form'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('find/', find_user, name='find_user'),
]