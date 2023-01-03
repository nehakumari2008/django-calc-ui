from django.urls import path

from . import views

urlpatterns = [
    path('add/<int:number1>/<int:number2>/', views.addition, name='add'),
    path('sub/<int:number1>/<int:number2>/', views.subtraction, name='sub'),
    path('mul/<int:number1>/<int:number2>/', views.multiplication, name='mul'),
    path('div/<int:number1>/<int:number2>/', views.division, name='div')
]