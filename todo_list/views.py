from django.shortcuts import render
from .models import list

def todolist(request):
    all_items = list.objects.all
    return render(request, 'home_todo.html', {'all_items':all_items})

def about(request):
    my_name = "AE"
    return render(request, 'about.html', {'name': my_name})
