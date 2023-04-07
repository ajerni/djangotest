from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('name/<display_name>', views.name, name='name'),
    path('param/', views.param, name='param'),
    path('form/', views.form, name='form'),
    path('usage/', views.usage, name='usage'),
    path('todolist/', views.todolist, name='todolist'),
    
]