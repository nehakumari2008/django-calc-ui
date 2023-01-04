from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    #path('add/<int:number1>/<int:number2>/', views.addition, name='addition'),
    path('add/', views.addition, name='addition'),
    path('sub/', views.subtraction, name='subtraction'),
    path('mul/', views.multiplication, name='multiplication'),
    path('div/', views.division, name='division'),
    # path('add', views.addition, name='add'),
    # path('sub', views.subtraction, name='sub'),
    # path('mul', views.multiplication, name='mul'),
    # path('div', views.division, name='div'),

]