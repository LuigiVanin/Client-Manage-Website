from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.crud, name='crud'),
    path('crud/delete/<int:client_id>', views.delete, name='delete'),
    path('crud/create/', views.create, name='create')
]