from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('name/<display_name>', views.name, name='name'),
    path('param/', views.param, name='param'),
    path('form/', views.form, name='form'),
    # path('usageshow/', views.usageshow, name='usageshow'),
]

htmx_urlpatterns = [
    path('htmx/', views.htmx, name='htmx'),
    path('check_username/', views.check_username, name='check_username'),
]

urlpatterns += htmx_urlpatterns