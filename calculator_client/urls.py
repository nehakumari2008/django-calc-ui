from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='viewAdd'),
    path('sub/', views.sub, name='viewSub'),
    path('mul/', views.mul, name='viewMul'),
    path('div/', views.div, name='viewDiv'),
    # path('add', views.addition, name='add'),
    # path('sub', views.subtraction, name='sub'),
    # path('mul', views.multiplication, name='mul'),
    # path('div', views.division, name='div'),
    # path('history/', views.history_view, name='history')
]