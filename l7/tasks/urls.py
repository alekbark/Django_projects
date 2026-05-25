from django.urls import path
from . import views

urlpatterns = [

    # PW16
    path('test/', views.show_request),

    # ↩️ Redirect CBV
    path(
        'go_to_tasks/',
        views.TaskRedirectView.as_view(),
        name='go_to_tasks'
    ),

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
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),

    # 🔎 Фильтрация по месяцу
    path('month/<int:year>/<int:month>/', views.TaskMonthArchiveView.as_view(), name='month_archive'),

    # 🔎 Фильтрация по году
    path('year/<int:year>/', views.TaskYearArchiveView.as_view(), name='year_archive'),

    # 🔎 Текущий день
    path('today/', views.TaskTodayArchiveView.as_view(), name='today_archive'),

]
