from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud, name='crud'),
    path('delete/<int:client_id>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('edit/<int:client_id>', views.edit, name='edit')
]