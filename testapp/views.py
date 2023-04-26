from django.shortcuts import render
from django.http.response import HttpResponse

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
        name = request.POST['my_inputs_name'] # request.POST.get('my_inputs_name')
        return render(request, 'form.html', {'name':name})
    else:
        return render(request, 'form.html', {})
    
# def usageshow(request):
#     import requests
#     response = requests.get('http:localhost:8000/courses/')
#     data = response.json()
#     data2 = data[0]
#     return render(request, 'usageshow.html', {'data':data, 'data2':data2})

def htmx(request):
    return render(request, 'htmx.html', {})

def check_username(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name == 'andi':
            return HttpResponse('<div style="color: red;">This username already exists</div>')
        else:
            return HttpResponse('<div style="color: green;">This username is available</div>')

