from django.urls import re_path, path
from . import views
from .views import protected_view

urlpatterns = [

    # PW16
    path('test/', views.show_request),

    # HW16
    path('login/', views.protected_view),

    # 📋 Список всех задач
    re_path(r'^$', views.task_list, name='task_list'),

    # 🔍 Детальный просмотр задачи по ID
    re_path(r'^(?P<id>\d+)/$', views.task_detail, name='task_detail'),

    # ➕ Создание новой задачи
    re_path(r'^create/$', views.task_create, name='task_create'),

    # ✏️ Обновление задачи
    re_path(r'^(?P<id>\d+)/update/$', views.task_update, name='task_update'),

    # ❌ Удаление задачи
    re_path(r'^(?P<id>\d+)/delete/$', views.task_delete, name='task_delete')

]