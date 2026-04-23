from django.urls import path, re_path
from . import views

urlpatterns = [
    # база
    path('', views.task_list, name='task_list'),
    path('task/<int:id>/', views.task_detail, name='task_detail'),

    # CRUD
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:id>/update/', views.task_update, name='task_update'),
    path('task/<int:id>/delete/', views.task_delete, name='task_delete'),

    # фильтры
    path('tasks/completed/', views.completed_tasks, name='completed_tasks'),
    path('tasks/active/', views.active_tasks, name='active_tasks'),

    # по дате
    re_path(r'^tasks/date/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.tasks_by_month),
    path('tasks/date/<int:year>/', views.tasks_by_year, name='task_by_year'),

    # пользовательские (если бы была авторизация)
    re_path(r'^tasks/user/(?P<username>[a-zA-Z0-9_]+)/$', views.user_tasks),

    # пагинация
    path('tasks/page/<int:page>/', views.task_list_paginated, name='task_list_paginated'),

    # slug (красивый url)
    path('task/<slug:slug>/', views.task_by_slug, name='task_by_slug'),
]