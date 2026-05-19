from django.urls import re_path, path
from . import views

urlpatterns = [

    # PW16
    path('test/', views.show_request),

    # HW16
    path('login/', views.protected_view),

    # 📋 Список всех задач
    path('', views.TaskListView.as_view(), name='task_list'),

    # 🔍 Детальный просмотр задачи по ID
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),

    # ➕ Создание новой задачи
    path('create/', views.TaskCreateView.as_view(), name='task_create'),

    # ✏️ Обновление задачи
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),

    # ❌ Удаление задачи
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete')

]