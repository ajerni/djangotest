from django.urls import path
from . import views

urlpatterns = [
    path('todolist', views.todolist, name='todolist'),
    path('about', views.about, name='about')
    
]