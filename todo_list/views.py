from django.shortcuts import render
from .models import list
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def todolist(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Itemm has been added to list.'))
            all_items = list.objects.all
            return render(request, 'home_todo.html', {'all_items':all_items})
    else:
        all_items = list.objects.all
        return render(request, 'home_todo.html', {'all_items':all_items})

def about(request):
    my_name = "AE"
    return render(request, 'about.html', {'name': my_name})
