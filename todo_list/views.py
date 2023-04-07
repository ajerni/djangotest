from django.shortcuts import render

def todolist(request):
    return render(request, 'todo_list.html', {})
