from django.urls import path
from . import views

# один универсальный маршрут для HW7
urlpatterns = [
    path('<str:model_name>/', views.universal_list),
]