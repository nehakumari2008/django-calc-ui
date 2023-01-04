from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('add/<int:number1>/<int:number2>/', views.addition, name='addition'),
    path('sub/<int:number1>/<int:number2>/', views.subtraction, name='subtraction'),
    path('mul/<int:number1>/<int:number2>/', views.multiplication, name='multiplication'),
    path('div/<int:number1>/<int:number2>/', views.division, name='division'),
    # path('add', views.addition, name='add'),
    # path('sub', views.subtraction, name='sub'),
    # path('mul', views.multiplication, name='mul'),
    # path('div', views.division, name='div'),
    # path('history/', views.history_view, name='history')
]