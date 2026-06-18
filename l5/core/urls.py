from django.urls import path
from . import views

urlpatterns = [
    path('icecream/create/', views.create_icecream),
    path('icecreams/create/', views.create_icecreams),

    path('feedback/', views.feedback_create, name='feedback_create'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),

    path('documents/upload/', views.upload_document, name='upload_document'),
    path('documents/', views.document_list, name='document_list'),

    path('<str:model_name>/', views.universal_list),
]