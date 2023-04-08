from django.shortcuts import render

def todolist(request):
    return render(request, 'home_todo.html', {})

def about(request):
    my_name = "AE"
    return render(request, 'about.html', {'name': my_name})
