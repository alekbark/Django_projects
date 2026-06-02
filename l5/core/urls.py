from django.urls import path
from . import views

# один универсальный маршрут для HW7
urlpatterns = [
    path('icecream/create/', views.create_icecream),
    path('icecreams/create/', views.create_icecreams),

    path('<str:model_name>/', views.universal_list),
]