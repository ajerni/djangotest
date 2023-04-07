from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html', {})

def name(request, display_name):
    return render(request, 'name.html', {'display_name':display_name})

def param(request):
    from testapp.mycode import meiername
    name = request.GET.get('name')
    meiername_result = meiername(name)
    return render(request, 'param.html', {'param_name':name, 'meiername_result':meiername_result})

def form(request):
    if request.method == "POST":
        name = request.POST['my_inputs_name']
        return render(request, 'form.html', {'name':name})
    else:
        return render(request, 'form.html', {})
    
def usage(request):
    response = requests.get('http://127.0.0.1:8000/courses/')
    data = response.json()
    data2 = data[0]
    return render(request, 'usage.html', {'data':data, 'data2':data2})

def todolist(request):
    return render(request, 'todolist.html', {})
