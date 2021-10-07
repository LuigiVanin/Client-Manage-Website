from django.urls import path
from . import views

urlpatterns = [
    path('',view=views.login, name='login'),
    path('logout/', views.logout, name='logout')
]