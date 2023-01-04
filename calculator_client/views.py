import json

from django.shortcuts import render
import requests


# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from calculator.models import Operation


def index(request):
    return render(request, 'base.html')


def add(request):
    if request.method == "POST":
        input1 = int(request.POST['num1'])
        input2 = int(request.POST['num2'])

        # Building the URL for API Call
        url = request.build_absolute_uri(reverse('addition'))

        # Serializing json data for POST request of the API
        post_data = json.dumps({'num1': input1, 'num2': input2})
        response = requests.post(url, data=post_data)

        # De-Serializing response json
        content = json.loads(response.content)
        result = content['sum']
        return render(request, 'result.html', {'result': result})
    return render(request, 'add.html')


def sub(request):
    if request.method == "POST":
        input1 = int(request.POST['num1'])
        input2 = int(request.POST['num2'])
        url = request.build_absolute_uri(reverse('subtraction'))

        # Serializing json data for POST request of the API
        post_data = json.dumps({'num1': input1, 'num2': input2})
        response = requests.post(url, data=post_data)

        # De-Serializing response json
        content = json.loads(response.content)
        result = content['diff']
        return render(request, 'result.html', {'result': result})
    return render(request, 'sub.html')


def mul(request):
    if request.method == "POST":
        input1 = int(request.POST['num1'])
        input2 = int(request.POST['num2'])
        url = request.build_absolute_uri(reverse('multiplication'))

        # Serializing json data for POST request of the API
        post_data = json.dumps({'num1': input1, 'num2': input2})
        response = requests.post(url, data=post_data)

        # De-Serializing response json
        content = json.loads(response.content)
        result = content['Multiplication']
        return render(request, 'result.html', {'result': result})
    return render(request, 'multiply.html')


def div(request):
    if request.method == "POST":
        input1 = int(request.POST['num1'])
        input2 = int(request.POST['num2'])
        url = request.build_absolute_uri(reverse('division'))

        # Serializing json data for POST request of the API
        post_data = json.dumps({'num1': input1, 'num2': input2})
        response = requests.post(url, data=post_data)

        # De-Serializing response json
        content = json.loads(response.content)
        result = content['division']
        return render(request, 'result.html', {'result': result})

    return render(request, 'div.html')


def history_view(request):
    history_objects = Operation.objects.all()
    return render(request, 'history.html', {'data': history_objects})