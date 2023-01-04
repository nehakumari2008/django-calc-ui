from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'base.html')


def add(request):
    return render(request, 'add.html')


def sub(request):
    return render(request, 'sub.html')


def mul(request):
    return render(request, 'multiply.html')


def div(request):
    return render(request, 'div.html')