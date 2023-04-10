from django.shortcuts import render, redirect
from .models import list
from .forms import ListForm
from django.contrib import messages

def todolist(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been added to list.'))
            all_items = list.objects.all
            return render(request, 'home_todo.html', {'all_items':all_items})
    else:
        all_items = list.objects.all
        return render(request, 'home_todo.html', {'all_items':all_items})
    
def delete(request, list_id):
    item = list.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted.'))
    return redirect('todolist')

def cross_off(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('todolist')

def uncross(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('todolist')

def edit(request, list_id):

    if request.method == 'POST':
        item = list.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited.'))
            return redirect('todolist')
    else:
        item = list.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item':item})

def about(request):
    my_name = "AE"
    return render(request, 'about.html', {'name': my_name})

