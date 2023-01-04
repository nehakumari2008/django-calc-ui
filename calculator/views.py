import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from calculator.models import Operation

def index(request):
    return render(request, 'input.html')


def addition(request):
    input1 = request.POST['First_number']
    input2 = request.POST['Second_number']
    res = input1 + input2
    calculate = Operation(First_number=input1, Second_number=input2, operator= '+', Result=res)
    calculate.save()

    return render(request, 'result.html', {"result": res})



def subtraction(request):
    diff = (number1 - number2)
    processed_data = {"num1": number1, "num2": number2, "difference": diff}
    json_object = json.dumps(processed_data, indent=4)
    return HttpResponse(json_object)


def multiplication(request, number2, number1):
    mul = (number1 * number2)
    processed_data = {"num1": number1, "num2": number2, "Multiplication": mul}
    json_object = json.dumps(processed_data, indent=4)
    return HttpResponse(json_object)


def division(request, number1, number2):
    try:
        div = (number1 / number2)
        processed_data = {"num1": number1, "num2": number2, "division": div}
        json_object = json.dumps(processed_data, indent=4)
        return HttpResponse(json_object)
    except:
        return HttpResponse("Cannot be divide by 0")


def history_view(request):
    show_history = operation.objects.all()
    return render(request, 'history.html', {'show history': show_history})