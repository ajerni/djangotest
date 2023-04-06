from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def name(request, display_name):
    return render(request, 'name.html', {'display_name':display_name})

def param(request):
    from testapp.mycode import meiername
    name = request.GET.get('name')
    meiername_result = meiername(name)
    return render(request, 'param.html', {'param_name':name, 'meiername_result':meiername_result})

def page_not_found_view(request):
    return render(request, '404.html', status=404)