from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('name/<display_name>', views.name, name='name'),
    path('param/', views.param, name='param')
    
]

hadler404 = 'testapp.views.page_not_found_view'