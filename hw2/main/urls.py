from django.urls import path
from . import views

urlpatterns = [
    path('', views.items_list),
    path('items/', views.items_list),
    path('items/<int:id>/', views.items_detail),
]